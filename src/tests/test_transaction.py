# tests/test_transaction.py

import unittest
from src.transaction import TransactionManager  # Assuming you have a TransactionManager class

class TestTransactionManager(unittest.TestCase):
    def setUp(self):
        self.tx_manager = TransactionManager()

    def test_create_transaction(self):
        tx = self.tx_manager.create_transaction(from_address='0xFromAddress', to_address='0xToAddress', amount=1.0)
        self.assertIsInstance(tx, dict)  # Check if the transaction is a dictionary
        self.assertIn('tx_id', tx)  # Check if transaction ID is present

    def test_validate_transaction(self):
        tx = self.tx_manager.create_transaction(from_address='0xFromAddress', to_address='0xToAddress', amount=1.0)
        is_valid = self.tx_manager.validate_transaction(tx)
        self.assertTrue(is_valid)  # Check if the transaction is valid

    def test_process_transaction(self):
        tx = self.tx_manager.create_transaction(from_address='0xFromAddress', to_address='0xToAddress', amount=1.0)
        result = self.tx_manager.process_transaction(tx)
        self.assertTrue(result['success'])  # Check if the transaction was processed successfully

if __name__ == '__main__':
    unittest.main()
