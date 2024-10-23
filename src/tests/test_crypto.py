# tests/test_crypto.py

import unittest
from src.crypto_utils import CryptoUtils  # Assuming you have a crypto_utils module

class TestCryptoUtils(unittest.TestCase):
    def setUp(self):
        self.crypto = CryptoUtils()

    def test_hash_function(self):
        data = "test data"
        hashed = self.crypto.hash(data)
        self.assertIsInstance(hashed, str)  # Check if the output is a string

    def test_signature_verification(self):
        private_key = "your_private_key"
        message = "test message"
        signature = self.crypto.sign(message, private_key)
        is_valid = self.crypto.verify_signature(message, signature, "your_public_key")
        self.assertTrue(is_valid)  # Check if the signature is valid

if __name__ == '__main__':
    unittest.main()
