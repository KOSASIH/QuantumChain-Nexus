# src/interoperability/adapter.py

from web3 import Web3

class BlockchainAdapter:
    def __init__(self, blockchain_url):
        self.web3 = Web3(Web3.HTTPProvider(blockchain_url))

    def get_balance(self, address):
        balance = self.web3.eth.get_balance(address)
        return self.web3.fromWei(balance, 'ether')

    def send_transaction(self, from_address, to_address, amount, private_key):
        nonce = self.web3.eth.getTransactionCount(from_address)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
        }
        signed_tx = self.web3.eth.account.signTransaction(tx, private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return tx_hash.hex()

# Example usage
if __name__ == "__main__":
    adapter = BlockchainAdapter(blockchain_url='https://blockchain-url')
    balance = adapter.get_balance('0xYourAddress')
    print(f"Balance: {balance} ETH")
    # Uncomment the following line to send a transaction
    # tx_hash = adapter.send_transaction('0xFromAddress', '0xToAddress', 0.1, 'YourPrivateKey')
    # print(f"Transaction Hash: {tx_hash}")
