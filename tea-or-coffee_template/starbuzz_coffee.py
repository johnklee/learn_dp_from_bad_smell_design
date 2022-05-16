"""StarBuzz Coffee recipe."""

import starbuzz_beverage
from typing import List


_STEP_MAKE_DRINK = 'Brew coffee in boiling water'
_STEP_ADD_CONDIMENT = 'Add sugar and milk'


class StarBuzzCoffee(starbuzz_beverage.CaffeineBeverage):
  def make_drink(self, action_list: List[str]):
    action_list.append(_STEP_MAKE_DRINK)

  def add_condiment(self, action_list: List[str]):
    action_list.append(_STEP_ADD_CONDIMENT)
  
  def is_coffee(self):
    return True