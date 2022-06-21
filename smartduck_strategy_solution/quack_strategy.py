class Quack:
  def __init__(self, sound):
    self.sound = sound

  def __call__(self):
    return f'{self.sound}!'
