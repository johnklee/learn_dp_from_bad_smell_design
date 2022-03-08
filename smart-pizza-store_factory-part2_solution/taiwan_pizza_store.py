import errors
import pizza_stores
import pizza_recipes
import taiwan_pizza_recipes


class TaiwanPizzaStore(pizza_stores.PizzaStore):
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
      raise errors.UnknownPizzaNameError(pizza_name)
