"""Unit test cases of smart home agent."""

import smart_home
import unittest


class TestSmartHomeAgent(unittest.TestCase):

  def setUp(self):
    super().setUp()
    self.sha = smart_home.SmartHomeAgent()

  def test_enter_home(self):
    self.sha.enter_home()

    self.assertTrue(self.sha._device_facade.is_lamp_on())
    self.assertTrue(self.sha._device_facade.is_tv_on())
    self.assertTrue(self.sha._device_facade.is_ac_on())

  def test_enter_bedroom_with_ac_on(self):
    self.sha._device_facade.turn_on_ac()

    self.sha.enter_bedroom()

    self.assertFalse(self.sha._device_facade.is_lamp_on())
    self.assertFalse(self.sha._device_facade.is_tv_on())
    self.assertTrue(self.sha._device_facade.is_ac_on())
    self.assertEqual(25, self.sha._device_facade.get_ac_degree())

  def test_enter_living_room_with_tv_on(self):
    self.sha._device_facade.turn_on_tv()

    self.sha.enter_living_room()

    self.assertTrue(self.sha._device_facade.is_lamp_on())
    self.assertTrue(self.sha._device_facade.is_tv_on())
    self.assertEqual(66, self.sha._device_facade.get_tv_channel())

  def test_exit_home_with_all_on(self):
    self.sha._device_facade.turn_on_ac()
    self.sha._device_facade.turn_on_tv()
    self.sha._device_facade.turn_on_lamp()

    self.sha.exit_home()

    self.assertFalse(self.sha._device_facade.is_lamp_on())
    self.assertFalse(self.sha._device_facade.is_tv_on())
    self.assertFalse(self.sha._device_facade.is_ac_on())


if __name__ == '__main__':
    unittest.main()
