"""StarBuzz Beverage recipes."""
import abc

from typing import List

_STEP_BOIL_WATER = 'Boil some water'
_STEP_PULL_DRINK = 'Pour drink in cup'
_STEP_GRIND_COFFEE_BEAN = 'Grind coffee bean'


class CaffeineBeverage(abc.ABC):
  """Receipe of Caffeine Beverage."""

  @abc.abstractmethod
  def make_drink(self, action_list: List[str]):
    raise NotImplementedError

  @abc.abstractmethod
  def add_condiment(self, action_list: List[str]):
    raise NotImplementedError

  def boil_water(self, action_list: List[str]):
    action_list.append(_STEP_BOIL_WATER)

  def pull_drink(self, action_list: List[str]):
    action_list.append(_STEP_PULL_DRINK)

  def is_coffee(self):
    return False

  def grind_coffee_bean(self, action_list: List[str]):
    action_list.append(_STEP_GRIND_COFFEE_BEAN)

  def make(self) -> List[str]:
    action_list = []
    if self.is_coffee():
      self.grind_coffee_bean(action_list)

    self.boil_water(action_list)
    self.make_drink(action_list)
    self.pull_drink(action_list)
    self.add_condiment(action_list)

    return action_list
