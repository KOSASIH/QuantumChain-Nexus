# scripts/deploy.py

from web3 import Web3
import json

class ContractDeployer:
    def __init__(self, blockchain_url, private_key):
        self.web3 = Web3(Web3.HTTPProvider(blockchain_url))
        self.private_key = private_key
        self.account = self.web3.eth.account.from_key(private_key)

    def deploy_contract(self, contract_interface, *args):
        # Create the contract instance
        contract = self.web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bytecode'])
        
        # Build the transaction
        transaction = contract.constructor(*args).buildTransaction({
            'chainId': 1,  # Mainnet
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
            'nonce': self.web3.eth.getTransactionCount(self.account.address),
        })

        # Sign the transaction
        signed_tx = self.web3.eth.account.signTransaction(transaction, self.private_key)

        # Send the transaction
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        print(f"Contract deployed! Transaction hash: {tx_hash.hex()}")

        # Wait for the transaction to be mined
        tx_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Contract deployed at address: {tx_receipt.contractAddress}")

# Example usage
if __name__ == "__main__":
    deployer = ContractDeployer(blockchain_url='https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID', private_key='YOUR_PRIVATE_KEY')
    with open('path/to/contract_interface.json') as f:
        contract_interface = json.load(f)
    deployer.deploy_contract(contract_interface, arg1, arg2)  # Pass constructor arguments as needed
