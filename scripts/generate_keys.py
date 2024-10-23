# scripts/generate_keys.py

from eth_account import Account

def generate_key_pair():
    # Generate a new Ethereum account
    account = Account.create()
    print(f"Address: {account.address}")
    print(f"Private Key: {account.privateKey.hex()}")

if __name__ == "__main__":
    generate_key_pair()
