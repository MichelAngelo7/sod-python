class Expenses:
  def __init__(self, name, value):
    self.name = name
    self.value = value

  def __str__(self):
    return f'Nome da dispesa: {self.name}, Valor da dispesa: {self.value}'