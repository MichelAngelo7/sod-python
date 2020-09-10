#!/usr/bin/python3
from datetime import datetime
from expenses import Expenses

def main():
  newExpenser = Expenses("Mercado Livre", -150)
  print(newExpenser)

if __name__ == "__main__":
    main()
