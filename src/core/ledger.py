# src/core/ledger.py

class Ledger:
    def __init__(self):
        self.blocks = []  # List to hold all blocks
        self.transactions = []  # List to hold all transactions

    def add_block(self, block):
        """Add a new block to the ledger."""
        self.blocks.append(block)

    def add_transaction(self, transaction):
        """Add a new transaction to the ledger."""
        self.transactions.append(transaction)

    def get_block(self, index):
        """Retrieve a block by its index."""
        if index < len(self.blocks):
            return self.blocks[index]
        return None  # Return None if the block does not exist

    def get_transaction(self, index):
        """Retrieve a transaction by its index."""
        if index < len(self.transactions):
            return self.transactions[index]
        return None  # Return None if the transaction does not exist

    def get_all_blocks(self):
        """Retrieve all blocks in the ledger."""
        return self.blocks

    def get_all_transactions(self):
        """Retrieve all transactions in the ledger."""
        return self.transactions

# Example usage
if __name__ == "__main__":
    ledger = Ledger()

    # Simulate adding blocks and transactions
    ledger.add_block({"index": 1, "transactions": [], "proof": 12345})
    ledger.add_block({"index": 2, "transactions": [], "proof": 67890})

    ledger.add_transaction({"sender": "Alice", "recipient": "Bob", "amount": 50})
    ledger.add_transaction({"sender": "Bob", "recipient": "Charlie", "amount": 30})

    print("All Blocks:")
    for block in ledger.get_all_blocks():
        print(block)

    print("\nAll Transactions:")
    for transaction in ledger.get_all_transactions():
        print(transaction)
