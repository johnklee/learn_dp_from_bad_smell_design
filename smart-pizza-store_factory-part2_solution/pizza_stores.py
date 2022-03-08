import abc
import errors
import pizza_recipes


class PizzaStore(abc.ABC):
  def order_pizza(self, pizza_name: str) -> pizza_recipes.Pizza:
    pizza = self.create_pizza(pizza_name)

    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza

  @abc.abstractmethod
  def create_pizza(self, pizza_name: str) -> pizza_recipes.Pizza:
    raise NotImplementedError()


class SimplePizzaStore(PizzaStore):
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
      raise errors.UnknownPizzaNameError(pizza_name)
