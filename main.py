# main.py
from transaction import Transaction
from user import User



# Example usage:
user1 = User("John Doe", "john@example.com")
#user1.make_deposit(100).make_withdrawal(20).display_user_balance()

user2 = User("Jane Smith", "jane@example.com")

#user2.make_deposit(200).make_withdrawal(50).display_user_balance()




# Create transactions for the first account
transactions1 = [
    Transaction(user1, {'transaction_type': 'deposit', 'amount': 100}),
    Transaction(user1, {'transaction_type': 'deposit', 'amount': 50}),
    Transaction(user1, {'transaction_type': 'deposit', 'amount': 250}),
    Transaction(user1, {'transaction_type': 'withdraw', 'amount': 20})
]

# Create transactions for the second account
transactions2 = [
    Transaction(user2, {'transaction_type': 'deposit', 'amount': 5000}),
    Transaction(user2, {'transaction_type': 'deposit', 'amount': 3500}),
    Transaction(user2, {'transaction_type': 'withdraw', 'amount': 250}),
    Transaction(user2, {'transaction_type': 'withdraw', 'amount': 500}),
    Transaction(user2, {'transaction_type': 'withdraw', 'amount': 1500}),
    Transaction(user2, {'transaction_type': 'withdraw', 'amount': 1200})
]

# Perform transactions for both accounts
Transaction.perform_transaction(transactions1 + transactions2)

# Interest calculation after all transactions
user1.yield_interest()
user2.yield_interest()

# Display account information after transactions
print(user1.display_user_info(),'\n',user2.display_user_info())




