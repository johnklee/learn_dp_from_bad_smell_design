"""Device API protocols."""

from abc import ABC, abstractmethod


class DeviceInterface(ABC):

  @abstractmethod
  def is_on(self):
    raise NotImplementedError('Subclasses should implement this!')


class TVInterface(DeviceInterface):

  @abstractmethod
  def get_channel(self):
    raise NotImplementedError('Subclasses should implement this!')


class ACInterface(DeviceInterface):

  @abstractmethod
  def get_degree(self):
    raise NotImplementedError('Subclasses should implement this!')
