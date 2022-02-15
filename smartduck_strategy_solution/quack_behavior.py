import abc


class QuackBehavior(abc.ABC):
  @abc.abstractmethod
  def quack(self) -> str:
    raise NotImplementedError


class Quack(QuackBehavior):
  def quack(self) -> str:
    return 'quack!'


class Squeak(QuackBehavior):
  def quack(self) -> str:
    return 'squeak!'
