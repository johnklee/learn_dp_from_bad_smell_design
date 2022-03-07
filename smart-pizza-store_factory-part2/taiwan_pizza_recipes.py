import pizza_recipes


class TaiwanCheezePizza(pizza_recipes.Pizza):
  def prepare(self):
    print('Add Cheeze and bacon')
    self.ingredients.append('blue cheeze')
    self.ingredients.append('bacon')

  def bake(self):
    print('Bake in light fire for 1.5 hours')

  def cut(self):
    print('Cut in 8 pieces')
    self.num_piece = 8

  def box(self):
    print('Use paper box')
    self.box_material = 'paper'


class TaiwanGreekPizza(pizza_recipes.Pizza):
  def prepare(self):
    print('Add special spicies and beef')
    self.ingredients.append('special spices')
    self.ingredients.append('Taiwan beef')

  def bake(self):
    print('Bake in mild fire for 1 hours')

  def cut(self):
    print('Cut in 8 pieces')
    self.num_piece = 8

  def box(self):
    print('Use paper box')
    self.box_material = 'paper'


class TaiwanPepperoniPizza(pizza_recipes.Pizza):
  def prepare(self):
    print('Add pepperoni and cuttlefish')
    self.ingredients.append('pepperoni')
    self.ingredients.append('cuttlefish')

  def bake(self):
    print('Bake in strong fire for 0.8 hours')

  def cut(self):
    print('Cut in 8 pieces')
    self.num_piece = 8

  def box(self):
    print('Use paper box')
    self.box_material = 'paper'


class TaiwanVeggiePizza(pizza_recipes.Pizza):
  def prepare(self):
    print('Add pickle and crab')
    self.ingredients.append('pickle')
    self.ingredients.append('crab')

  def bake(self):
    print('Bake in light fire for 4 hours')

  def cut(self):
    print('Cut in 8 pieces')
    self.num_piece = 8

  def box(self):
    print('Use paper box')
    self.box_material = 'paper'
