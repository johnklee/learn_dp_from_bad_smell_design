import pizza_recipes
import pizza_ingredients
import pizza_ingredients_factory


class TaiwanIngredientsFactory(pizza_ingredients_factory.PizzaIngredientFactory):
  def create_topping(self) -> pizza_ingredients.Topping:
    return pizza_ingredients.SpinachTopping()

  def create_dough(self) -> pizza_ingredients.Dough:
    return pizza_ingredients.ThinCrustDough()

  def create_sauce(self) -> pizza_ingredients.Sauce:
    return pizza_ingredients.MarinaraSauce()

  def create_cheese(self) -> pizza_ingredients.Cheese:
    return pizza_ingredients.ReggianCheese()

  def create_clams(self) -> pizza_ingredients.Clams:
    return pizza_ingredients.FreshClams()

  def create_oil(self) -> pizza_ingredients.Oil:
    return pizza_ingredients.OliveOil()
