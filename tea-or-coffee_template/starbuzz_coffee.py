"""StarBuzz Coffee recipe."""

from typing import List
from starbuzz_beverage import CaffeineBeverage

_STEP_MAKE_DRINK = 'Brew coffee in boiling water'
_STEP_ADD_CONDIMENT = 'Add sugar and milk'


class StarBuzzCoffee(CaffeineBeverage):

  def is_coffee(self):
    return True

  def make_drink(self, action_list: List[str]):
    action_list.append(_STEP_MAKE_DRINK)
    return action_list
  
  def add_condiment(self, action_list: List[str]):
    action_list.append(_STEP_ADD_CONDIMENT)
