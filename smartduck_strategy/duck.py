class Duck:
  def quack(self):
    return 'quack!'

  def swim(self):
    return 'I can swim!'

  def display(self):
    return 'I am a duck!'


class MallardDuck(Duck):
  def display(self):
    return 'I am a mallard duck ^^'


class RedheadDuck(Duck):
  def display(self):
    return 'I am a redhead duck @_@'


class RubberDuck(Duck):
  def quack(self):
    return 'squeak!'

  def display(self):
    return 'I am a rubber duck ><"'
