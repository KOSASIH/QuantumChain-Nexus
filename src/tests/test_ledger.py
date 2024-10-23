# tests/test_ledger.py

import unittest
from src.ledger import LedgerManager  # Assuming you have a LedgerManager class

class TestLedgerManager(unittest.TestCase):
    def setUp(self):
        self.ledger_manager = LedgerManager()

    def test_add_entry(self):
        entry = self.ledger_manager.add_entry(transaction_id='tx123', amount=1.0, from_address='0xFromAddress', to_address='0xToAddress')
        self.assertIsInstance(entry, dict)  # Check if the entry is a dictionary
        self.assertIn('entry_id', entry)  # Check if entry ID is present

    def test_get_entry(self):
        entry = self.ledger_manager.add_entry(transaction_id='tx123', amount=1.0, from_address='0xFromAddress', to_address='0xToAddress')
        retrieved_entry = self.ledger_manager.get_entry(entry['entry_id'])
        self.assertEqual(retrieved_entry['transaction_id'], 'tx123')  # Check if the retrieved entry matches

    def test_validate_ledger(self):
        self.ledger_manager.add_entry(transaction_id='tx123', amount=1.0, from_address='0xFromAddress', to_address='0xToAddress')
        is_valid = self.ledger_manager.validate_ledger()
        self.assertTrue(is_valid)  # Check if the ledger is valid

if __name__ == '__main__':
    unittest.main()
