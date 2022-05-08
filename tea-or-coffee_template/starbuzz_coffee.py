"""StarBuzz Coffee recipe."""

from typing import List

_STEP_BOIL_WATER = 'Boil some water'
_STEP_MAKE_DRINK = 'Brew coffee in boiling water'
_STEP_PULL_DRINK = 'Pour coffee in cup'
_STEP_ADD_CONDIMENT = 'Add sugar and milk'


class StarBuzzCoffee:
  def make(self) -> List[str]:
    action_list = []
    action_list.append(_STEP_BOIL_WATER)
    action_list.append(_STEP_MAKE_DRINK)
    action_list.append(_STEP_PULL_DRINK)
    action_list.append(_STEP_ADD_CONDIMENT)

    return action_list
