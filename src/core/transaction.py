# src/core/transaction.py

import hashlib
import json

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = int(time.time())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transaction_data = {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp,
        }
        transaction_string = json.dumps(transaction_data, sort_keys=True)
        return hashlib.sha256(transaction_string.encode()).hexdigest()

    def to_dict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp,
            "hash": self.hash,
        }

class TransactionHandler:
    def __init__(self):
        self.transactions = []

    def create_transaction(self, sender, recipient, amount):
        transaction = Transaction(sender, recipient, amount)
        self.transactions.append(transaction)
        return transaction

    def validate_transaction(self, transaction):
        # Implement transaction validation logic (e.g., check sender balance, etc.)
        # For simplicity, we assume the transaction is valid if the sender and recipient are not the same
        return transaction.sender != transaction.recipient

    def execute_transaction(self, transaction):
        # Implement transaction execution logic (e.g., update sender and recipient balances, etc.)
        # For simplicity, we assume the transaction is executed successfully
        return True

# Example usage
if __name__ == "__main__":
    transaction_handler = TransactionHandler()
    transaction = transaction_handler.create_transaction("Alice", "Bob", 50)
    print(transaction.to_dict())

    is_valid = transaction_handler.validate_transaction(transaction)
    print(f"Is the transaction valid? {is_valid}")

    is_executed = transaction_handler.execute_transaction(transaction)
    print(f"Is the transaction executed? {is_executed}")
