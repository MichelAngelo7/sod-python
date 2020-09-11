from people import People

class User(People):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.expenses = []

  def register_expenses(self, expense):
    self.expenses.append(expense)