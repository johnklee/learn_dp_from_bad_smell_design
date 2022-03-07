import abc
import pizza_recipes


class Error(Exception):
  pass


class UnknownPizzaNameError(Error):
  def __init__(self, name):
    super().__init__(f'Pizza name={name} is unknown!')


class PizzaFactory(abc.ABC):
  @abc.abstractmethod
  def create_pizza(self, pizza_name: str) -> pizza_recipes.Pizza:
    raise NotImplementedError


class SimpleFactory(PizzaFactory):
  def create_pizza(self, pizza_name: str) -> pizza_recipes.Pizza:
    if pizza_name == 'cheeze':
      return pizza_recipes.CheezePizza()
    elif pizza_name == 'greek':
      return pizza_recipes.GreekPizza()
    elif pizza_name == 'pepper':
      return pizza_recipes.PepperoniPizza()
    elif pizza_name == 'veg':
      return pizza_recipes.VeggiePizza()
    else:
      raise UnknownPizzaNameError(pizza_name)
