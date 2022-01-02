"""Unit test cases of smart home agent."""

import smart_home
import unittest


class TestSmartHomeAgent(unittest.TestCase):

  def setUp(self):
    super().setUp()
    self.sha = smart_home.SmartHomeAgent()

  def test_enter_home(self):
    self.sha.enter_home()

    self.assertTrue(self.sha.lamp_ctr.is_on())
    self.assertTrue(self.sha.tv_ctr.is_on())
    self.assertTrue(self.sha.ac_ctr.is_on())

  def test_enter_bedroom_with_ac_on(self):
    self.sha.ac_ctr.turn_on()

    self.sha.enter_bedroom()

    self.assertFalse(self.sha.lamp_ctr.is_on())
    self.assertFalse(self.sha.tv_ctr.is_on())
    self.assertTrue(self.sha.ac_ctr.is_on())
    self.assertEqual(25, self.sha.ac_ctr.get_degree())

  def test_enter_living_room_with_tv_on(self):
    self.sha.tv_ctr.turn_on()

    self.sha.enter_living_room()

    self.assertTrue(self.sha.lamp_ctr.is_on())
    self.assertTrue(self.sha.tv_ctr.is_on())
    self.assertEqual(66, self.sha.tv_ctr.get_channel())

  def test_exit_home_with_all_on(self):
    self.sha.ac_ctr.turn_on()
    self.sha.tv_ctr.turn_on()
    self.sha.lamp_ctr.turn_on()

    self.sha.exit_home()

    self.assertFalse(self.sha.lamp_ctr.is_on())
    self.assertFalse(self.sha.tv_ctr.is_on())
    self.assertFalse(self.sha.ac_ctr.is_on())


if __name__ == '__main__':
    unittest.main()
