import abc


class FlyBehavior(abc.ABC):
  @abc.abstractmethod
  def fly(self) -> str:
    raise NotImplementedError


class Flyable(FlyBehavior):
  def fly(self) -> str:
    return 'I can fly!'


class FlyNoWay(FlyBehavior):
  def fly(self) -> str:
    return 'I can not fly!'
