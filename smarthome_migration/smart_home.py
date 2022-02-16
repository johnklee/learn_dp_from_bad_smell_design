"""Smart Home Agent."""

from log_utils import get_logger
import facade


class SmartHomeAgent:
  def __init__(self):
    self.prefered_degree = 23
    self.device_facade = facade.SmartHomeDeviceFacade(self.prefered_degree)
    self.log = get_logger(self)

  def enter_home(self):
    self.log.info('Entering home...')
    self.device_facade.turn_on_lamp()
    self.device_facade.turn_on_ac()
    self.device_facade.turn_on_tv()

  def enter_bedroom(self):
    self.log.info('Entering bedroom...')
    self.device_facade.turn_off_lamp()
    self.device_facade.turn_off_tv()
    if self.device_facade.is_ac_on():
      self.device_facade.set_ac_degree(25)

  def enter_living_room(self):
    self.log.info('Entering living room...')
    self.device_facade.turn_on_lamp()
    if self.device_facade.is_tv_on():
      self.device_facade.set_tv_channel(66)

  def exit_home(self):
    self.log.info('Exiting home...')
    self.device_facade.turn_off_lamp()
    self.device_facade.turn_off_tv()
    self.device_facade.turn_off_ac()

  def self_test(self):
    self.enter_home()
    self.enter_bedroom()
    self.enter_living_room()
    self.exit_home()


if __name__ == '__main__':
  print('=== Testing Smart Home Agent ===')
  sha = SmartHomeAgent()
  sha.self_test()
