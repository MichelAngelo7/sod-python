#!/usr/bin/python3
from datetime import datetime
from expenses import Expenses
from user import User

def main():
  newUser = User("Michel", 31)
  expense1 = Expenses("Mercado livre", -150)
  expense2 = Expenses("Super Mercado" , -45.34)
  newCard =  (newUser.name, datetime(2020, 8, 30), 'Mercado SA', 5, 350.00, 'Lanch')  

  print(newUser)

  
  newUser.register_expenses(expense1)
  newUser.register_expenses(expense2)
  

  total_newUser = newUser.total_expense()

  print(newCard)

if __name__ == "__main__":
    main()
