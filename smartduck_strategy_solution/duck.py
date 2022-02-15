import fly_behavior
import quack_behavior


class Duck:
  def __init__(self, fly_strategy=None, quack_strategy=None):
    self.fly_strategy = fly_strategy if fly_strategy else fly_behavior.Flyable()
    self.quack_strategy = quack_strategy if quack_strategy else quack_behavior.Quack()

  def quack(self):
    return self.quack_strategy.quack()

  def swim(self):
    return 'I can swim!'

  def display(self):
    return 'I am a duck!'

  def fly(self):
    return self.fly_strategy.fly()


class MallardDuck(Duck):
  def display(self):
    return 'I am a mallard duck ^^'


class RedheadDuck(Duck):
  def display(self):
    return 'I am a redhead duck @_@'


class RubberDuck(Duck):
  def __init__(self):
    super().__init__(
        fly_behavior.FlyNoWay(),
        quack_behavior.Squeak())

  def display(self):
    return 'I am a rubber duck ><"'


class DecoyDuck(Duck):
  def __init__(self):
    super().__init__(
        fly_behavior.FlyNoWay(),
        quack_behavior.Squeak())

  def display(self):
    return 'I am a decoy duck :p'
