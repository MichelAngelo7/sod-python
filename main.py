#!/usr/bin/python3
from datetime import datetime
from expenses import Expenses
from user import User

def main():
  newUser = User("Michel", 31)
  newExpense = Expenses("Mercado livre", -150)
  
  print(newUser)
  print(newExpense)

  newUser.register_expenses(newExpense)




if __name__ == "__main__":
    main()
