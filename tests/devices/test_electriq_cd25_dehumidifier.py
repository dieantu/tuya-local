from homeassistant.components.fan import SUPPORT_PRESET_MODE
from homeassistant.components.humidifier import SUPPORT_MODES
from homeassistant.const import (
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_TEMPERATURE,
    PERCENTAGE,
    TEMP_CELSIUS,
)

from ..const import ELECTRIQ_DEHUMIDIFIER_PAYLOAD
from ..helpers import assert_device_properties_set
from ..mixins.light import BasicLightTests
from ..mixins.lock import BasicLockTests
from ..mixins.sensor import MultiSensorTests
from ..mixins.switch import BasicSwitchTests, SwitchableTests
from .base_device_tests import TuyaDeviceTestCase

SWITCH_DPS = "1"
MODE_DPS = "2"
CURRENTHUMID_DPS = "3"
HUMIDITY_DPS = "4"
LOCK_DPS = "7"
LIGHT_DPS = "10"
PRESET_DPS = "102"
CURRENTTEMP_DPS = "103"
IONIZER_DPS = "104"


class TestElectriqCD25ProDehumidifier(
    BasicLightTests,
    BasicLockTests,
    BasicSwitchTests,
    MultiSensorTests,
    SwitchableTests,
    TuyaDeviceTestCase,
):
    __test__ = True

    def setUp(self):
        self.setUpForConfig(
            "electriq_cd25pro_dehumidifier.yaml", ELECTRIQ_DEHUMIDIFIER_PAYLOAD
        )
        self.subject = self.entities.get("humidifier")
        self.fan = self.entities.get("fan")
        self.setUpSwitchable(SWITCH_DPS, self.subject)
        self.setUpBasicLight(LIGHT_DPS, self.entities.get("light_uv_sterilization"))
        self.setUpBasicLock(LOCK_DPS, self.entities.get("lock_child_lock"))
        self.setUpBasicSwitch(IONIZER_DPS, self.entities.get("switch_ionizer"))
        self.setUpMultiSensors(
            [
                {
                    "name": "sensor_current_temperature",
                    "dps": CURRENTTEMP_DPS,
                    "unit": TEMP_CELSIUS,
                    "device_class": DEVICE_CLASS_TEMPERATURE,
                    "state_class": "measurement",
                },
                {
                    "name": "sensor_current_humidity",
                    "dps": CURRENTHUMID_DPS,
                    "unit": PERCENTAGE,
                    "device_class": DEVICE_CLASS_HUMIDITY,
                    "state_class": "measurement",
                },
            ]
        )
        self.mark_secondary(["lock_child_lock"])

    def test_supported_features(self):
        self.assertEqual(self.subject.supported_features, SUPPORT_MODES)
        self.assertEqual(self.fan.supported_features, SUPPORT_PRESET_MODE)

    def test_icon(self):
        """Test that the icon is as expected."""
        self.dps[SWITCH_DPS] = True
        self.dps[MODE_DPS] = "auto"
        self.assertEqual(self.subject.icon, "mdi:air-humidifier")

        self.dps[SWITCH_DPS] = False
        self.assertEqual(self.subject.icon, "mdi:air-humidifier-off")

        self.dps[MODE_DPS] = "fan"
        self.assertEqual(self.subject.icon, "mdi:air-humidifier-off")

        self.dps[SWITCH_DPS] = True
        self.assertEqual(self.subject.icon, "mdi:air-purifier")

        self.dps[MODE_DPS] = "high"
        self.assertEqual(self.subject.icon, "mdi:tshirt-crew-outline")

        self.assertEqual(self.basicLight.icon, "mdi:solar-power")
        self.assertEqual(self.basicSwitch.icon, "mdi:creation")

    def test_min_target_humidity(self):
        self.assertEqual(self.subject.min_humidity, 35)

    def test_max_target_humidity(self):
        self.assertEqual(self.subject.max_humidity, 80)

    def test_target_humidity(self):
        self.dps[HUMIDITY_DPS] = 55
        self.assertEqual(self.subject.target_humidity, 55)

    async def test_set_target_humidity_rounds_up_to_5_percent(self):
        async with assert_device_properties_set(
            self.subject._device,
            {HUMIDITY_DPS: 55},
        ):
            await self.subject.async_set_humidity(53)

    async def test_set_target_humidity_rounds_down_to_5_percent(self):
        async with assert_device_properties_set(
            self.subject._device,
            {HUMIDITY_DPS: 50},
        ):
            await self.subject.async_set_humidity(52)

    async def test_fan_turn_on(self):
        async with assert_device_properties_set(
            self.subject._device, {SWITCH_DPS: True}
        ):
            await self.fan.async_turn_on()

    async def test_fan_turn_off(self):
        async with assert_device_properties_set(
            self.subject._device, {SWITCH_DPS: False}
        ):
            await self.fan.async_turn_off()

    def test_mode(self):
        self.dps[MODE_DPS] = "low"
        self.assertEqual(self.subject.mode, "Low")
        self.dps[MODE_DPS] = "high"
        self.assertEqual(self.subject.mode, "High")
        self.dps[MODE_DPS] = "auto"
        self.assertEqual(self.subject.mode, "Auto")
        self.dps[MODE_DPS] = "fan"
        self.assertEqual(self.subject.mode, "Air clean")

    async def test_set_mode_to_auto(self):
        async with assert_device_properties_set(
            self.subject._device,
            {
                MODE_DPS: "auto",
            },
        ):
            await self.subject.async_set_mode("Auto")
            self.subject._device.anticipate_property_value.assert_not_called()

    async def test_set_mode_to_low(self):
        async with assert_device_properties_set(
            self.subject._device,
            {
                MODE_DPS: "low",
            },
        ):
            await self.subject.async_set_mode("Low")
            self.subject._device.anticipate_property_value.assert_not_called()

    async def test_set_mode_to_high(self):
        async with assert_device_properties_set(
            self.subject._device,
            {
                MODE_DPS: "high",
            },
        ):
            await self.subject.async_set_mode("High")
            self.subject._device.anticipate_property_value.assert_not_called()

    async def test_set_mode_to_fan(self):
        async with assert_device_properties_set(
            self.subject._device,
            {
                MODE_DPS: "fan",
            },
        ):
            await self.subject.async_set_mode("Air clean")
            self.subject._device.anticipate_property_value.assert_not_called()

    def test_fan_preset_mode(self):
        self.dps[PRESET_DPS] = "45"
        self.assertEqual(self.fan.preset_mode, "Half open")

        self.dps[PRESET_DPS] = "90"
        self.assertEqual(self.fan.preset_mode, "Fully open")

        self.dps[PRESET_DPS] = "0_90"
        self.assertEqual(self.fan.preset_mode, "Oscillate")

    async def test_set_fan_to_half_open(self):
        async with assert_device_properties_set(
            self.subject._device,
            {
                PRESET_DPS: "45",
            },
        ):
            await self.fan.async_set_preset_mode("Half open")
            self.subject._device.anticipate_property_value.assert_not_called()

    async def test_set_fan_to_fully_open(self):
        async with assert_device_properties_set(
            self.subject._device,
            {
                PRESET_DPS: "90",
            },
        ):
            await self.fan.async_set_preset_mode("Fully open")
            self.subject._device.anticipate_property_value.assert_not_called()

    async def test_set_fan_to_oscillate(self):
        async with assert_device_properties_set(
            self.subject._device,
            {
                PRESET_DPS: "0_90",
            },
        ):
            await self.fan.async_set_preset_mode("Oscillate")
            self.subject._device.anticipate_property_value.assert_not_called()

    def test_extra_state_attributes(self):
        self.dps[CURRENTHUMID_DPS] = 50
        self.dps[CURRENTTEMP_DPS] = 21
        self.assertDictEqual(
            self.subject.extra_state_attributes,
            {"current_humidity": 50, "current_temperature": 21},
        )
        self.assertEqual(self.fan.extra_state_attributes, {})
