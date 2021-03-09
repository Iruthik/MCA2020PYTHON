# 2.  Create a Bank account with members account number, name, type of account and balance.
# Write constructor and methods to deposit at the bank and withdraw an amount from the bank.


class Bank_Account:
   def __init__(self):
      self.balance=0
      print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

   def deposit(self):
      amount = float(input("Enter amount to be Deposited: "))
      self.balance += amount
      print("\n Amount Deposited:",amount)

   def withdraw(self):
      amount = float(input("Enter amount to be Withdrawn: "))
      if self.balance>=amount:
         self.balance-=amount
         print("\n You Withdrew:", amount)
      else:
         print("\n Insufficient balance ")

   def display(self):
      print("\n Net Available Balance=",self.balance)


s = Bank_Account()
s.deposit()
s.withdraw()
s.display()