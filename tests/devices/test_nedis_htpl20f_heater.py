from homeassistant.components.climate.const import (
    HVAC_MODE_HEAT,
    HVAC_MODE_OFF,
    PRESET_AWAY,
    PRESET_COMFORT,
    PRESET_ECO,
    SUPPORT_TARGET_TEMPERATURE,
    SUPPORT_PRESET_MODE,
)
from homeassistant.const import STATE_UNAVAILABLE, TIME_MINUTES

from ..const import NEDIS_HTPL20F_PAYLOAD
from ..helpers import assert_device_properties_set
from ..mixins.climate import TargetTemperatureTests
from ..mixins.lock import BasicLockTests
from ..mixins.number import BasicNumberTests
from .base_device_tests import TuyaDeviceTestCase

HVACMODE_DPS = "1"
TEMPERATURE_DPS = "2"
CURRENTTEMP_DPS = "3"
PRESET_DPS = "4"
LOCK_DPS = "7"
UNKNOWN11_DPS = "11"
TIMER_DPS = "13"
UNKNOWN101_DPS = "101"


class TestNedisHtpl20fHeater(
    BasicLockTests, BasicNumberTests, TargetTemperatureTests, TuyaDeviceTestCase
):
    __test__ = True

    def setUp(self):
        self.setUpForConfig("nedis_htpl20f_heater.yaml", NEDIS_HTPL20F_PAYLOAD)
        self.subject = self.entities.get("climate")
        self.setUpTargetTemperature(
            TEMPERATURE_DPS,
            self.subject,
            min=15,
            max=35,
        )
        self.setUpBasicLock(
            LOCK_DPS,
            self.entities.get("lock_child_lock"),
        )
        self.setUpBasicNumber(
            TIMER_DPS,
            self.entities.get("number_timer"),
            max=1440,
            unit=TIME_MINUTES,
        )
        self.mark_secondary(["lock_child_lock", "number_timer"])

    def test_supported_features(self):
        self.assertEqual(
            self.subject.supported_features,
            SUPPORT_TARGET_TEMPERATURE | SUPPORT_PRESET_MODE,
        )

    def test_icon(self):
        self.dps[HVACMODE_DPS] = True
        self.assertEqual(self.subject.icon, "mdi:radiator")

        self.dps[HVACMODE_DPS] = False
        self.assertEqual(self.subject.icon, "mdi:radiator-disabled")

    def test_temperature_unit_returns_device_temperature_unit(self):
        self.assertEqual(
            self.subject.temperature_unit, self.subject._device.temperature_unit
        )

    def test_current_temperature(self):
        self.dps[CURRENTTEMP_DPS] = 25
        self.assertEqual(self.subject.current_temperature, 25)

    def test_hvac_mode(self):
        self.dps[HVACMODE_DPS] = True
        self.assertEqual(self.subject.hvac_mode, HVAC_MODE_HEAT)

        self.dps[HVACMODE_DPS] = False
        self.assertEqual(self.subject.hvac_mode, HVAC_MODE_OFF)

        self.dps[HVACMODE_DPS] = None
        self.assertEqual(self.subject.hvac_mode, STATE_UNAVAILABLE)

    def test_hvac_modes(self):
        self.assertCountEqual(self.subject.hvac_modes, [HVAC_MODE_OFF, HVAC_MODE_HEAT])

    async def test_turn_on(self):
        async with assert_device_properties_set(
            self.subject._device, {HVACMODE_DPS: True}
        ):
            await self.subject.async_set_hvac_mode(HVAC_MODE_HEAT)

    async def test_turn_off(self):
        async with assert_device_properties_set(
            self.subject._device, {HVACMODE_DPS: False}
        ):
            await self.subject.async_set_hvac_mode(HVAC_MODE_OFF)

    def test_preset_modes(self):
        self.assertCountEqual(
            self.subject.preset_modes,
            [PRESET_COMFORT, PRESET_ECO, PRESET_AWAY],
        )

    def test_preset_mode(self):
        self.dps[PRESET_DPS] = "1"
        self.assertEqual(self.subject.preset_mode, PRESET_ECO)

        self.dps[PRESET_DPS] = "2"
        self.assertEqual(self.subject.preset_mode, PRESET_COMFORT)

        self.dps[PRESET_DPS] = "3"
        self.assertEqual(self.subject.preset_mode, PRESET_AWAY)

    async def test_set_preset_more_to_eco(self):
        async with assert_device_properties_set(
            self.subject._device, {PRESET_DPS: "1"}
        ):
            await self.subject.async_set_preset_mode(PRESET_ECO)

    async def test_set_preset_more_to_comfort(self):
        async with assert_device_properties_set(
            self.subject._device, {PRESET_DPS: "2"}
        ):
            await self.subject.async_set_preset_mode(PRESET_COMFORT)

    async def test_set_preset_more_to_away(self):
        async with assert_device_properties_set(
            self.subject._device, {PRESET_DPS: "3"}
        ):
            await self.subject.async_set_preset_mode(PRESET_AWAY)

    def test_extra_state_attributes(self):
        self.dps[UNKNOWN11_DPS] = "11"
        self.dps[UNKNOWN101_DPS] = True

        self.assertCountEqual(
            self.subject.extra_state_attributes,
            {"unknown_11": "11", "unknown_101": True},
        )
