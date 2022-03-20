import abc
import errors
import pizza_recipes
import pizza_ingredients_factory


class PizzaStore:
  def order_pizza(self, pizza_name: str) -> pizza_recipes.Pizza:
    pizza = self.create_pizza(pizza_name)

    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza

  @abc.abstractmethod
  def create_pizza(self, pizza_name: str) -> pizza_recipes.Pizza:
    raise NotImplementedError


class SimplePizzaStore(PizzaStore):
  def __init__(self):
    self.ifactory = pizza_ingredients_factory.SimpleIngredientFactory()
    self.regisrered_pizza_flavor = {
      'cheese': pizza_recipes.CheezePizza(self.ifactory),
      'greek': pizza_recipes.GreekPizza(self.ifactory),
      'pepper': pizza_recipes.PepperoniPizza(self.ifactory),
      'veg': pizza_recipes.VeggiePizza(self.ifactory),
    }

  def create_pizza(self, pizza_name: str) -> pizza_recipes.Pizza:
    try:
      return self.regisrered_pizza_flavor[pizza_name]
    except KeyError as e:
      raise errors.UnknownPizzaNameError(pizza_name)
