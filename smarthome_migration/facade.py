from log_utils import get_logger
import lamp_device
import tv_device
import ac_device


class SmartHomeDeviceFacade:
  
  def __init__(self, prefered_degree: int) -> None:
    self.lamp_ctr = lamp_device.LEDLightController('Kitchen')
    self.tv_ctr = tv_device.LEDTVController('Kitchen')
    self.ac_ctr = ac_device.ACControllerV2()
    self.log = get_logger(self)
    self.prefered_degree = prefered_degree

  def turn_on_lamp(self) -> None:
    self.lamp_ctr.on()

  def turn_on_tv(self) -> None:
    self.tv_ctr.on()

  def turn_on_ac(self) -> None:
    self.ac_ctr.on(self.prefered_degree)

  def is_lamp_on(self) -> None:
    self.lamp_ctr.is_on()
  
  def is_tv_on(self) -> None:
    self.tv_ctr.is_on()
  
  def is_ac_on(self) -> None:
    self.ac_ctr.is_on()

  def turn_off_lamp(self) -> None:
    self.lamp_ctr.off()

  def turn_off_tv(self) -> None:
    self.tv_ctr.off()

  def turn_off_ac(self) -> None:
    self.ac_ctr.off()

  def set_ac_degree(self, degree: int) -> None:
    self.degree = degree
    self.ac_ctr.degree = self.degree
  
  def get_ac_degree(self) -> None:
    self.ac_ctr.get_degree()
  
  def set_tv_channel(self, channel: int) -> None:
    self.channel = channel
    self.tv_ctr.channel_num = self.channel
  
  def get_tv_channel(self) -> None:
    self.tv_ctr.get_channel()


  