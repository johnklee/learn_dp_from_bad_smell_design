"""Smart Home Agent."""

from log_utils import get_logger
import lamp_device
import tv_device
import ac_device


class SmartHomeAgent:
  def __init__(self):
    self.lamp_ctr = lamp_device.LampControllerV1('Kitchen')
    self.tv_ctr = tv_device.TVController('Kitchen')
    self.ac_ctr = ac_device.ACControllerV1()
    self.log = get_logger(self)
    self.prefered_degree = 20

  def enter_home(self):
    self.log.info('Entering home...')
    self.lamp_ctr.turn_on()
    self.tv_ctr.turn_on()
    self.ac_ctr.turn_on(self.prefered_degree)

  def enter_bedroom(self):
    self.log.info('Entering bedroom...')
    self.lamp_ctr.turn_off()
    self.tv_ctr.turn_off()
    if self.ac_ctr.is_on():
      self.ac_ctr.turn_degree(25)

  def enter_living_room(self):
    self.log.info('Entering living room...')
    self.lamp_ctr.turn_on()
    if self.tv_ctr.is_on():
      self.tv_ctr.switch_channel_to(66)

  def exit_home(self):
    self.log.info('Exiting home...')
    self.lamp_ctr.turn_off()
    self.tv_ctr.turn_off()
    self.ac_ctr.turn_off()

  def self_test(self):
    self.enter_home()
    self.enter_bedroom()
    self.enter_living_room()
    self.exit_home()


if __name__ == '__main__':
  print('=== Testing Smart Home Agent ===')
  sha = SmartHomeAgent()
  sha.self_test()
