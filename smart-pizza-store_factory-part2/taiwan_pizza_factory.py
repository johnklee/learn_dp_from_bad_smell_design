import pizza_recipes
import pizza_factory
import taiwan_pizza_recipes


class Error(Exception):
  pass


class UnknownPizzaNameError(Error):
  def __init__(self, name):
    super().__init__(f'Pizza name={name} is unknown!')


class TaiwanFactory(pizza_factory.PizzaFactory):
  def create_pizza(self, pizza_name: str) -> pizza_recipes.Pizza:
    if pizza_name == 'cheeze':
      return taiwan_pizza_recipes.TaiwanCheezePizza()
    elif pizza_name == 'greek':
      return taiwan_pizza_recipes.TaiwanGreekPizza()
    elif pizza_name == 'pepper':
      return taiwan_pizza_recipes.TaiwanPepperoniPizza()
    elif pizza_name == 'veg':
      return taiwan_pizza_recipes.TaiwanVeggiePizza()
    else:
      raise UnknownPizzaNameError(pizza_name)
