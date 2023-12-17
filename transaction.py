# transaction.py

class Transaction:
    def __init__(self, user, transaction_data):
        self.user = user
        self.transaction_data = transaction_data

    @staticmethod
    def perform_transaction(transactions):
        for transaction in transactions:
            transaction_handlers = {
                'deposit': transaction.user.deposit,
                'withdraw': transaction.user.withdraw
            }

            transaction_type = transaction.transaction_data.get('transaction_type')
            amount = transaction.transaction_data.get('amount')

            transaction_handler = transaction_handlers.get(transaction_type)
            if transaction_handler and amount is not None:
                transaction_handler(amount)
