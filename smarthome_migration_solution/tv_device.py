"""Television controller."""

import device_api
from log_utils import get_logger


class TVController(device_api.TVInterface):
  def __init__(self, location, default_channel_num=10):
    self.location = location
    self.on_state = False
    self.channel_num = default_channel_num
    self.log = get_logger(self)

  def is_on(self):
    return self.on_state

  def get_channel(self):
    return self.channel_num

  def turn_on(self):
    if not self.on_state:
      self.log.info('\tTurn on TV(%s) with channel=%d', self.location, self.channel_num)
      self.on_state = True

  def turn_off(self):
    if self.on_state:
      self.log.info('\tTurn off TV(%s)', self.location)
      self.on_state = False

  def switch_channel_to(self, channel_num):
    if self.on_state:
      self.log.info(
          '\tSwitch TV(%s) to channel=%d', self.location, channel_num)
      self.channel_num = channel_num
    else:
      self.log.warning('Please turn on TV first!')


class LEDTVController(device_api.TVInterface):
  def __init__(self, location):
    self.location = location
    self._on_state = False
    self._channel_num = 10
    self.log = get_logger(self)

  def is_on(self):
    return self.on_state

  def get_channel(self):
    return self._channel_num

  @property
  def on_state(self):
    return self._on_state

  @on_state.setter
  def on_state(self, val):
    if self._on_state ^ val:
      state_str = 'on' if val else 'off'
      self.log.info(
          '\tTurn %s TV(%s) with channel=%d',
          state_str, self.location, self.channel_num)
      self._on_state = val

  @property
  def channel_num(self):
    return self._channel_num

  @channel_num.setter
  def channel_num(self, val):
    if not self.on_state:
      self.log.warning('\tPlease turn on first!')
      return

    if self._channel_num != val:
      self._channel_num = val
      self.log.info(
          '\tChange channel of TV(%s) to be %d',
          self.location, self._channel_num)

  def on(self):
    self.on_state = True

  def off(self):
    self.on_state = False
