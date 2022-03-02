import pizza_recipes


class PizzaStore:
  def __init__(self, factory):
    self.factory = factory

  def order_pizza(self, pizza_name: str) -> pizza_recipes.Pizza:
    pizza = self.factory.create_pizza(pizza_name)

    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
    return pizza
