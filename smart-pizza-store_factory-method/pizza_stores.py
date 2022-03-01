import pizza_recipes


def order_pizza(type:str) -> pizza_recipes.Pizza:
  if type == 'cheeze':
    pizza = pizza_recipes.CheezePizza()
  elif type == 'greek':
    pizza = pizza_recipes.GreekPizza()

  pizza.prepare()
  pizza.bake()
  pizza.cut()
  pizza.box()
  return pizza
