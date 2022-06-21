class Fly:
  def __call__(self):
    return 'I can fly!'


class NoFly:
  def __call__(self):
    return 'I can not fly!'


def get_fly_behavior(can_fly: bool=True):
  if can_fly: return Fly()
  else: return NoFly()
