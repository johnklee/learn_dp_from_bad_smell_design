"""Main program of StarBuzz."""

import starbuzz_coffee
import starbuzz_tea


def make_coffee():
  coffee_recipe = starbuzz_coffee.StarBuzzCoffee()
  return '\n'.join(coffee_recipe.make())


def make_tea():
  tea_recipe = starbuzz_tea.StarBuzzTea()
  return '\n'.join(tea_recipe.make())


if __name__ == '__main__':
  print('Order coffee:')
  print(make_coffee() + '\n\n')
  print('Order tea:')
  print(make_tea() + '\n\n')
