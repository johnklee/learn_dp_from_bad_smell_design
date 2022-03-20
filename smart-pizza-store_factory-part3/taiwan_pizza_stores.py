import errors
import pizza_recipes
import pizza_stores
import taiwan_pizza_recipes
import taiwan_pizza_ingredients_factory


class TaiwanPizzaStore(pizza_stores.PizzaStore):
  def __init__(self):
    self.ifactory = taiwan_pizza_ingredients_factory.TaiwanIngredientsFactory()
    self.regisrered_pizza_flavor = {
      'cheese': taiwan_pizza_recipes.TaiwanCheezePizza(self.ifactory),
      'greek': taiwan_pizza_recipes.TaiwanGreekPizza(self.ifactory),
      'pepper': taiwan_pizza_recipes.TaiwanPepperoniPizza(self.ifactory),
      'veg': taiwan_pizza_recipes.TaiwanVeggiePizza(self.ifactory),
      'hidden_menu': taiwan_pizza_recipes.TaiwanHiddenMenuPizza(self.ifactory),
    }

  def create_pizza(self, pizza_name: str) -> pizza_recipes.Pizza:
    try:
      return self.regisrered_pizza_flavor[pizza_name]
    except KeyError as e:
      raise errors.UnknownPizzaNameError(pizza_name)
