"""Facade module to encapsulate operations from all devices."""

from log_utils import get_logger
import lamp_device
import tv_device
import ac_device


class HomeDeviceFacade:
  """Home devices facade."""

  def __init__(self, prefered_degree: int):
    self._lamp_ctr = lamp_device.LEDLightController('Kitchen')
    self._tv_ctr = tv_device.LEDTVController('Kitchen')
    self._ac_ctr = ac_device.ACControllerV2()
    self.log = get_logger(self)
    self._prefered_degree = prefered_degree

  def turn_off_all_devices(self):
    self.turn_off_lamp()
    self.turn_off_tv()
    self.turn_off_ac()

  def turn_on_lamp(self):
    self._lamp_ctr.on()

  def turn_on_tv(self):
    self._tv_ctr.on()

  def turn_on_ac(self):
    self._ac_ctr.on(self._prefered_degree)

  def turn_off_lamp(self):
    self._lamp_ctr.off()

  def turn_off_tv(self):
    self._tv_ctr.off()

  def turn_off_ac(self):
    self._ac_ctr.off()

  def set_ac_degree(self, degree: int):
    self._ac_ctr.degree = degree

  def switch_tv_channel(self, channel: int):
    self._tv_ctr.channel_num = channel

  def is_ac_on(self) -> bool:
    return self._ac_ctr.is_on()

  def is_tv_on(self) -> bool:
    return self._tv_ctr.is_on()

  def is_lamp_on(self) -> bool:
    return self._lamp_ctr.is_on()

  def get_ac_degree(self) -> int:
    return self._ac_ctr.get_degree()

  def get_tv_channel(self) -> int:
    return self._tv_ctr.channel_num
