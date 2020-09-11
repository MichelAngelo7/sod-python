from people import People

class User(People):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.expenses = []

  def __str__(self):
    return f'Nome: {self.name}, Idade: {self.age}'

  def register_expenses(self, expense):
    self.expenses.append(expense)

  def total_expense(self):
    total = 0
    for expense in self.expenses:
      total += expense.value
    return total

