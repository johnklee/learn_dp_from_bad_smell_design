import abc
import pizza_ingredients


class PizzaIngredientFactory(abc.ABC):
  @abc.abstractmethod
  def create_topping(self) -> pizza_ingredients.Topping:
    raise NotImplementedError

  @abc.abstractmethod
  def create_dough(self) -> pizza_ingredients.Dough:
    raise NotImplementedError

  @abc.abstractmethod
  def create_sauce(self) -> pizza_ingredients.Sauce:
    raise NotImplementedError

  @abc.abstractmethod
  def create_cheese(self) -> pizza_ingredients.Cheese:
    raise NotImplementedError

  @abc.abstractmethod
  def create_clams(self) -> pizza_ingredients.Clams:
    raise NotImplementedError


class SimpleIngredientFactory(PizzaIngredientFactory):
  def create_topping(self) -> pizza_ingredients.Topping:
    return pizza_ingredients.SausageTopping()

  def create_pepperoni_topping(self) -> pizza_ingredients.Topping:
    return pizza_ingredients.PepperoniTopping()

  def create_veggie_topping(self) -> pizza_ingredients.Topping:
    return pizza_ingredients.VeggieTopping()

  def create_dough(self) -> pizza_ingredients.Dough:
    return pizza_ingredients.ThickCrustDough()

  def create_sauce(self) -> pizza_ingredients.Sauce:
    return pizza_ingredients.KetchupSauce()

  def create_cheese(self) -> pizza_ingredients.Cheese:
    return pizza_ingredients.SakuraCheese()

  def create_clams(self) -> pizza_ingredients.Clams:
    return pizza_ingredients.SoftshellClams()
