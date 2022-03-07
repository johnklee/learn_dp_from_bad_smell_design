import abc


class Pizza(abc.ABC):
  def __init__(self):
    self.ingredients = []
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
    print('Add Cheeze and bacon')
    self.ingredients.append('cheeze')
    self.ingredients.append('bacon')

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
    self.ingredients.append('special spices')
    self.ingredients.append('beef')

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
    self.ingredients.append('pepperoni')
    self.ingredients.append('seafood')

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
    self.ingredients.append('veggie')
    self.ingredients.append('bread')

  def bake(self):
    print('Bake in light fire for 3 hours')

  def cut(self):
    print('Cut in 8 pieces')
    self.num_piece = 8

  def box(self):
    print('Use paper box')
    self.box_material = 'paper'
