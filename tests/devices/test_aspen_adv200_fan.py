from homeassistant.components.climate.const import (
    HVAC_MODE_FAN_ONLY,
    HVAC_MODE_OFF,
    SUPPORT_TARGET_TEMPERATURE,
)
from homeassistant.components.fan import (
    DIRECTION_FORWARD,
    DIRECTION_REVERSE,
    SUPPORT_DIRECTION,
    SUPPORT_PRESET_MODE,
    SUPPORT_SET_SPEED,
)
from homeassistant.const import TEMP_FAHRENHEIT

from ..const import ASPEN_ASP200_FAN_PAYLOAD
from ..helpers import assert_device_properties_set
from ..mixins.climate import TargetTemperatureTests
from ..mixins.light import DimmableLightTests
from ..mixins.switch import SwitchableTests
from .base_device_tests import TuyaDeviceTestCase

SWITCH_DPS = "1"
DIRECTION_DPS = "2"
SPEED_DPS = "3"
UNKNOWN8_DPS = "8"
TEMPERATURE_DPS = "18"
CURTEMP_DPS = "19"
PRESET_DPS = "101"
LIGHT_DPS = "102"


class TestAspenASP200Fan(
    DimmableLightTests, SwitchableTests, TargetTemperatureTests, TuyaDeviceTestCase
):
    __test__ = True

    def setUp(self):
        self.setUpForConfig("aspen_asp200_fan.yaml", ASPEN_ASP200_FAN_PAYLOAD)
        self.subject = self.entities.get("fan")
        self.climate = self.entities.get("climate")
        self.setUpDimmableLight(
            LIGHT_DPS,
            self.entities.get("light_display"),
            offval=0,
            tests=[
                (1, 85),
                (2, 170),
                (3, 255),
            ],
        )
        self.setUpSwitchable(SWITCH_DPS, self.subject)
        self.setUpTargetTemperature(
            TEMPERATURE_DPS,
            self.climate,
            min=40,
            max=95,
        )
        self.mark_secondary(["light_display"])

    def test_supported_features(self):
        self.assertEqual(
            self.subject.supported_features,
            SUPPORT_DIRECTION | SUPPORT_PRESET_MODE | SUPPORT_SET_SPEED,
        )
        self.assertEqual(
            self.climate.supported_features,
            SUPPORT_TARGET_TEMPERATURE,
        )

    def test_fan_direction(self):
        self.dps[DIRECTION_DPS] = "in"
        self.assertEqual(self.subject.current_direction, DIRECTION_FORWARD)
        self.dps[DIRECTION_DPS] = "out"
        self.assertEqual(self.subject.current_direction, DIRECTION_REVERSE)
        self.dps[DIRECTION_DPS] = "exch"
        self.assertEqual(self.subject.current_direction, "exchange")

    async def test_fan_set_direction_forward(self):
        async with assert_device_properties_set(
            self.subject._device, {DIRECTION_DPS: "in"}
        ):
            await self.subject.async_set_direction(DIRECTION_FORWARD)

    async def test_fan_set_direction_reverse(self):
        async with assert_device_properties_set(
            self.subject._device, {DIRECTION_DPS: "out"}
        ):
            await self.subject.async_set_direction(DIRECTION_REVERSE)

    async def test_fan_set_direction_exchange(self):
        async with assert_device_properties_set(
            self.subject._device, {DIRECTION_DPS: "exch"}
        ):
            await self.subject.async_set_direction("exchange")

    def test_fan_speed(self):
        self.dps[SPEED_DPS] = "1"
        self.assertAlmostEqual(self.subject.percentage, 33.3, 1)
        self.dps[SPEED_DPS] = "2"
        self.assertAlmostEqual(self.subject.percentage, 66.7, 1)
        self.dps[SPEED_DPS] = "3"
        self.assertEqual(self.subject.percentage, 100)

    def test_fan_speed_step(self):
        self.assertAlmostEqual(self.subject.percentage_step, 33.33, 2)
        self.assertEqual(self.subject.speed_count, 3)

    async def test_fan_set_speed(self):
        async with assert_device_properties_set(
            self.subject._device,
            {SPEED_DPS: 1},
        ):
            await self.subject.async_set_percentage(33)

    async def test_fan_set_speed_snaps(self):
        async with assert_device_properties_set(
            self.subject._device,
            {SPEED_DPS: 2},
        ):
            await self.subject.async_set_percentage(80)

    def test_fan_preset_modes(self):
        self.assertCountEqual(self.subject.preset_modes, ["constant", "auto"])

    def test_fan_preset_mode(self):
        self.dps[PRESET_DPS] = False
        self.assertEqual(self.subject.preset_mode, "constant")
        self.dps[PRESET_DPS] = True
        self.assertEqual(self.subject.preset_mode, "auto")

    async def test_fan_set_preset_to_constant(self):
        async with assert_device_properties_set(
            self.subject._device,
            {PRESET_DPS: False},
        ):
            await self.subject.async_set_preset_mode("constant")

    async def test_fan_set_preset_to_auto(self):
        async with assert_device_properties_set(
            self.subject._device,
            {PRESET_DPS: True},
        ):
            await self.subject.async_set_preset_mode("auto")

    def test_climate_current_temperature(self):
        self.dps[CURTEMP_DPS] = 24
        self.assertEqual(self.climate.current_temperature, 24)

    def test_climate_temperature_unit(self):
        self.assertEqual(self.climate.temperature_unit, TEMP_FAHRENHEIT)

    def test_climate_hvac_mode(self):
        self.dps[SWITCH_DPS] = False
        self.assertEqual(self.climate.hvac_mode, HVAC_MODE_OFF)
        self.dps[SWITCH_DPS] = True
        self.assertEqual(self.climate.hvac_mode, HVAC_MODE_FAN_ONLY)

    def test_climate_hvac_modes(self):
        self.assertCountEqual(
            self.climate.hvac_modes,
            [HVAC_MODE_FAN_ONLY, HVAC_MODE_OFF],
        )

    async def test_climate_turn_on(self):
        async with assert_device_properties_set(
            self.climate._device,
            {SWITCH_DPS: True},
        ):
            await self.climate.async_set_hvac_mode(HVAC_MODE_FAN_ONLY)

    async def test_climate_turn_off(self):
        async with assert_device_properties_set(
            self.climate._device,
            {SWITCH_DPS: False},
        ):
            await self.climate.async_set_hvac_mode(HVAC_MODE_OFF)

    def test_extra_state_attributes(self):
        self.dps[UNKNOWN8_DPS] = 8
        self.assertDictEqual(self.subject.extra_state_attributes, {"unknown_8": 8})
        self.assertEqual(self.climate.extra_state_attributes, {})
