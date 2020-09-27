from people import People
from credit_card import CreditCard

class User(People):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.expenses = []

class CreditCard(CreditCard):
  def __init__(self, dateOfPurchase, creditorCompany=None,
                 numberOfInstallments=0, InstallmentsValue=0, category=None):
      super().__init__(dateOfPurchase=0, creditorCompany=None, 
      numberOfInstallments=0, InstallmentsValue=0, category=None)              
      self.creadCard = []

  def __str__(self):
    return f'Nome: {self.name}, Idade: {self.age}'

  def register_expenses(self, expense):
    self.expenses.append(expense)

  def total_expense(self):
    total = 0
    for expense in self.expenses:
      total += expense.value
    return total

