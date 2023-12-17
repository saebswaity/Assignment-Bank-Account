# bank_account.py

class BankAccount:
    def __init__(self, balance=0, int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        return f"Balance: ${self.balance}"

    def yield_interest(self):
        if self.balance > 0:
            interest_earned = self.balance * self.int_rate
            self.balance += interest_earned
        return self
