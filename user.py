# user.py
from bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0) 
    def deposit(self, amount):
        self.account.deposit(amount)  # Access BankAccount methods through association
        return self

    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    
    def yield_interest(self):
        return self.account.yield_interest()
        


    def display_user_info(self):
        return f"User: {self.name},\nEmail: {self.email},\nAccount info: {self.account.display_account_info()}"


