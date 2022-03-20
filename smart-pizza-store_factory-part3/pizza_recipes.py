import abc
import pizza_ingredients_factory


class Pizza(abc.ABC):
  def __init__(self, ifactory: pizza_ingredients_factory.PizzaIngredientFactory):
    self.ifactory = ifactory
    self.topping = None
    self.dough = None
    self.sauce = None
    self.cheese = None
    self.clams = None
    self.num_piece = -1
    self.box_material = None

  @abc.abstractmethod
  def prepare(self):
    raise NotImplementedError

  @abc.abstractmethod
  def bake(self):
    raise NotImplementedError

  @abc.abstractmethod
  def cut(self):
    raise NotImplementedError

  @abc.abstractmethod
  def box(self):
    raise NotImplementedError


class CheezePizza(Pizza):
  def prepare(self):
    self.cheese = self.ifactory.create_cheese()
    self.dough = self.ifactory.create_dough()
    self.sauce = self.ifactory.create_sauce()

  def bake(self):
    print('Bake in light fire for 2 hours')

  def cut(self):
    print('Cut in 6 pieces')
    self.num_piece = 6

  def box(self):
    print('Use paper box')
    self.box_material = 'paper'


class GreekPizza(Pizza):
  def prepare(self):
    print('Add special spicies and beef')
    self.cheese = self.ifactory.create_cheese()
    self.dough = self.ifactory.create_dough()
    self.sauce = self.ifactory.create_sauce()
    self.topping = self.ifactory.create_topping()

  def bake(self):
    print('Bake in mild fire for 1 hours')

  def cut(self):
    print('Cut in 8 pieces')
    self.num_piece = 8

  def box(self):
    print('Use plate')
    self.box_material = 'plate'


class PepperoniPizza(Pizza):
  def prepare(self):
    print('Add pepperoni and seafood')
    self.cheese = self.ifactory.create_cheese()
    self.dough = self.ifactory.create_dough()
    self.topping = self.ifactory.create_pepperoni_topping()
    self.clams = self.ifactory.create_clams()

  def bake(self):
    print('Bake in strong fire for 1 hours')

  def cut(self):
    print('Cut in 4 pieces')
    self.num_piece = 4

  def box(self):
    print('Use plastic box')
    self.box_material = 'plastic'


class VeggiePizza(Pizza):
  def prepare(self):
    print('Add veggie and bread')
    self.cheese = self.ifactory.create_cheese()
    self.dough = self.ifactory.create_dough()
    self.topping = self.ifactory.create_veggie_topping()

  def bake(self):
    print('Bake in light fire for 3 hours')

  def cut(self):
    print('Cut in 8 pieces')
    self.num_piece = 8

  def box(self):
    print('Use paper box')
    self.box_material = 'paper'
