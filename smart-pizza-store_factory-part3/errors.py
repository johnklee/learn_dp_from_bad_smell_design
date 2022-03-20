class Error(Exception):
  pass


class UnknownPizzaNameError(Error):
  def __init__(self, name):
    super().__init__(f'Pizza name={name} is unknown!')
