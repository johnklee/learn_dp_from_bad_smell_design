"""StarBuzz Coffee recipe."""

from typing import List
from starbuzz_beverage import CaffeineBeverage

_STEP_MAKE_DRINK = 'Steep tea in boiling water'
_STEP_ADD_CONDIMENT = 'Add lemon'


class StarBuzzTea(CaffeineBeverage):

  def make_drink(self, action_list: List[str]):
    action_list.append(_STEP_MAKE_DRINK)
    return action_list

  def add_condiment(self, action_list: List[str]):
    action_list.append(_STEP_ADD_CONDIMENT)
    return action_list
