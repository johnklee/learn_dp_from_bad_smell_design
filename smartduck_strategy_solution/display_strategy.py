class Display:
  def __init__(self, message):
    self.message = message

  def __call__(self):
    return self.message
