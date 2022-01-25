"""Lamp device controller."""

import device_api
from log_utils import get_logger
from termcolor import  colored, cprint


class LampControllerV1(device_api.DeviceInterface):
  def __init__(self, name):
    self.name = name
    self.log = get_logger(self)
    self.on_state = False

  def is_on(self):
    return self.on_state

  def turn_on(self):
    if not self.on_state:
      self.log.info('\tTurn on lamp(%s)', self.name)
      self.on_state = True

  def turn_off(self):
    if self.on_state:
      self.log.info('\tTurn off lamp(%s)', self.name)
      self.on_state = False


class LEDLightController:
  def __init__(self, name):
    self.name = name
    self.log = get_logger(self)
    self.on_state = False

  def is_on(self):
    return self.on_state

  def on(self, color='green'):
    if not self.on_state:
      self.log.info('\tTurn on LED light(%s)', self.name)
      cprint('LED Light blinking...', color, attrs = ['blink'])
      self.on_state = True

  def off(self):
    if self.on_state:
      self.log.info('\tTurn off LED light(%s)', self.name)
      self.on_state = False


class LEDLightControllerV2:
  def __init__(self, name):
    self.name = name
    self.log = get_logger(self)
    self._state = device_api.PowerState.OFF

  def is_on(self):
    return self._state == device_api.PowerState.ON

  def on(self, color='green'):
    if not self.is_on():
      self.log.info('\tTurn on LED light(%s)', self.name)
      cprint('LED Light blinking...', color, attrs = ['blink'])
      self._state = device_api.PowerState.ON

  def off(self):
    if self.is_on():
      self.log.info('\tTurn off LED light(%s)', self.name)
      self._state = device_api.PowerState.OFF
