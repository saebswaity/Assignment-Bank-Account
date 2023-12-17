class BankAccount:
    def __init__(self, balance=0, interest_rate=0.01):
        self.balance = balance
        self.interest_rate = interest_rate

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
        print(f"Balance: ${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            interest_earned = self.balance * self.interest_rate
            self.balance += interest_earned
        return self


class Transaction:
    def __init__(self, account, transaction_data):
        self.account = account
        self.transaction_data = transaction_data

    @staticmethod

    def perform_transaction(transactions):
        for transaction in transactions:
            transaction_handlers = {
                'deposit': transaction.account.deposit,
                'withdraw': transaction.account.withdraw
            }
        
            transaction_type = transaction.transaction_data.get('transaction_type')
            amount = transaction.transaction_data.get('amount')

            transaction_handler = transaction_handlers.get(transaction_type)
            if transaction_handler and amount is not None:
                transaction_handler(amount)



# Create the first account
account1 = BankAccount()

# Create the second account with a starting balance of $5000 and a custom interest rate of 0.03
account2 = BankAccount(balance=5000, interest_rate=0.03)


# Create transactions for the first account
transactions1 = [
    Transaction(account1, {'transaction_type': 'deposit', 'amount': 100}),
    Transaction(account1, {'transaction_type': 'deposit', 'amount': 50}),
    Transaction(account1, {'transaction_type': 'deposit', 'amount': 250}),
    Transaction(account1, {'transaction_type': 'withdraw', 'amount': 20})
]

# Create transactions for the second account
transactions2 = [
    Transaction(account2, {'transaction_type': 'deposit', 'amount': 5000}),
    Transaction(account2, {'transaction_type': 'deposit', 'amount': 3500}),
    Transaction(account2, {'transaction_type': 'withdraw', 'amount': 250}),
    Transaction(account2, {'transaction_type': 'withdraw', 'amount': 500}),
    Transaction(account2, {'transaction_type': 'withdraw', 'amount': 1500}),
    Transaction(account2, {'transaction_type': 'withdraw', 'amount': 1200})
]


Transaction.perform_transaction(transactions1 + transactions2 )

account1.yield_interest()
account2.yield_interest()
account1.display_account_info()
account2.display_account_info()

