import quack_strategy
import display_strategy
import fly_strategy


class Duck:
  def __init__(self, quack_sound: str='quack',
               display_message: str='I am a duck!', is_flyable: bool=True):
    self.quack = quack_strategy.Quack(quack_sound)
    self.display = display_strategy.Display(display_message)
    self.fly = fly_strategy.get_fly_behavior(is_flyable)

  def swim(self):
    return 'I can swim!'


class MallardDuck(Duck):
  def __init__(self):
    super().__init__(display_message='I am a mallard duck ^^')


class RedheadDuck(Duck):
  def __init__(self):
    super().__init__(display_message='I am a redhead duck @_@')


class RubberDuck(Duck):
  def __init__(self):
    super().__init__(quack_sound='squeak',
                     display_message='I am a rubber duck ><"',
                     is_flyable=False)


class DecoyDuck(Duck):
  def __init__(self):
    super().__init__(quack_sound='...',
                     display_message='I am a decoy duck :p',
                     is_flyable=False)
