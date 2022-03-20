import pizza_recipes


class TaiwanCheezePizza(pizza_recipes.Pizza):
  def prepare(self):
    print('Add Cheeze and bacon')
    self.cheese = self.ifactory.create_cheese()
    self.dough = self.ifactory.create_dough()
    self.sauce = self.ifactory.create_sauce()

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
    print('Use paper box')
    self.box_material = 'paper'


class TaiwanPepperoniPizza(pizza_recipes.Pizza):
  def prepare(self):
    print('Add pepperoni and cuttlefish')
    self.cheese = self.ifactory.create_cheese()
    self.dough = self.ifactory.create_dough()
    self.topping = self.ifactory.create_topping()
    self.clams = self.ifactory.create_clams()

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
    self.cheese = self.ifactory.create_cheese()
    self.dough = self.ifactory.create_dough()
    self.topping = self.ifactory.create_topping()

  def bake(self):
    print('Bake in light fire for 4 hours')

  def cut(self):
    print('Cut in 8 pieces')
    self.num_piece = 8

  def box(self):
    print('Use paper box')
    self.box_material = 'paper'


class TaiwanHiddenMenuPizza(pizza_recipes.Pizza):
  def prepare(self):
    print('Add pickle, beef and olive oil')
    self.cheese = self.ifactory.create_cheese()
    self.dough = self.ifactory.create_dough()
    self.topping = self.ifactory.create_topping()
    self.oil = self.ifactory.create_oil()

  def bake(self):
    print('Bake in light fire for 5 hours')

  def cut(self):
    print('Cut in 8 pieces')
    self.num_piece = 8

  def box(self):
    print('Use paper box')
    self.box_material = 'paper'
