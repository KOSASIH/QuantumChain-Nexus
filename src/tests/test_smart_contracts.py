# tests/test_smart_contracts.py

import unittest
from web3 import Web3
from src.smart_contracts.insurance import compile_insurance

class TestSmartContracts(unittest.TestCase):
    def setUp(self):
        self.web3 = Web3(Web3.HTTPProvider('https://blockchain-url'))
        self.contract_interface = compile_insurance()
        self.contract = self.web3.eth.contract(address='0xContractAddress', abi=self.contract_interface['abi'])

    def test_create_policy(self):
        # This test should be run with caution as it interacts with the blockchain
        # Uncomment the following lines to run the test
        # tx_hash = self.contract.functions.createPolicy(1000000000000000000, 10000000000000000000, 3600).transact({'from': '0xYourAddress', 'value': 1000000000000000000})
        # self.assertIsInstance(tx_hash, str)  # Check if transaction hash is a string

    def test_file_claim(self):
        # This test should be run with caution as it interacts with the blockchain
        # Uncomment the following lines to run the test
        # tx_hash = self.contract.functions.fileClaim(1).transact({'from': '0xYourAddress'})
        # self.assertIsInstance(tx_hash, str)  # Check if transaction hash is a string

if __name__ == '__main__':
    unittest.main()
