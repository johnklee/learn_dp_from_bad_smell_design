"""Air condition controller."""

import device_api
from log_utils import get_logger


class ACControllerV1(device_api.ACInterface):
  def __init__(self):
    self.on_state = False
    self.log = get_logger(self)
    self.degree = 20

  def is_on(self):
    return self.on_state

  def get_degree(self):
    return self.degree

  def turn_on(self, degree=None):
    if not self.on_state:
      if degree is None:
        degree = self.degree
      else:
        self.degree = degree
      self.log.info('\tTurn on AC at degree=%d', self.degree)
      self.on_state = True

  def turn_off(self):
    if self.on_state:
      self.log.info('\tTurn off AC...')
      self.on_state = False

  def turn_degree(self, degree):
    if self.on_state:
      self.log.info('\tTurning degree to be %d', degree)
      self.degree = degree
    else:
      self.log.warning('\tPlease turn on AC first!')


class ACControllerV2(device_api.ACInterface):
  def __init__(self):
    self.on_state = False
    self.log = get_logger(self)
    self._degree = 20

  def is_on(self):
    return self.on_state

  def get_degree(self):
    return self.degree

  def on(self, degree=None):
    if not self.on_state:
      self.log.info('\tTurn on AC')
      self.on_state = True
      degree = self._degree
      if degree is not None:
        self.degree = degree

  def off(self):
    if self.on_state:
      self.log.info('\tTurn off AC...')
      self.on_state = False

  @property
  def degree(self):
    return self._degree

  @degree.setter
  def degree(self, val):
    if self.on_state:
      self.log.info('\tTurning degree to be %d', val)
      self._degree = val
    else:
      self.log.warning('\tPlease turn on AC first!')
