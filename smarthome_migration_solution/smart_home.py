"""Smart Home Agent."""

from log_utils import get_logger
import device_facade


class SmartHomeAgent:
  def __init__(self):
    self.prefered_degree = 20
    self._device_facade = device_facade.HomeDeviceFacade(
        self.prefered_degree)
    self.log = get_logger(self)

  def enter_home(self):
    self.log.info('Entering home...')
    self._device_facade.turn_on_lamp()
    self._device_facade.turn_on_tv()
    self._device_facade.turn_on_ac()

  def enter_bedroom(self):
    self.log.info('Entering bedroom...')
    self._device_facade.turn_off_lamp()
    self._device_facade.turn_off_tv()
    if self._device_facade.is_ac_on():
      self._device_facade.set_ac_degree(25)

  def enter_living_room(self):
    self.log.info('Entering living room...')
    self._device_facade.turn_on_lamp()
    if self._device_facade.is_tv_on():
      self._device_facade.switch_tv_channel(66)

  def exit_home(self):
    self.log.info('Exiting home...')
    self._device_facade.turn_off_all_devices()

  def self_test(self):
    self.enter_home()
    self.enter_bedroom()
    self.enter_living_room()
    self.exit_home()


if __name__ == '__main__':
  print('=== Testing Smart Home Agent ===')
  sha = SmartHomeAgent()
  sha.self_test()
