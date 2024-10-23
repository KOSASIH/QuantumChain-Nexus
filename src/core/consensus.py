# src/core/consensus.py

import hashlib
import random

class ProofOfStake:
    def __init__(self):
        self.stakers = {}  # Dictionary to hold staker addresses and their stakes

    def register_staker(self, address, stake):
        """Register a staker with their stake."""
        if address in self.stakers:
            self.stakers[address] += stake  # Increase stake if already registered
        else:
            self.stakers[address] = stake

    def select_validator(self):
        """Select a validator based on their stake."""
        total_stake = sum(self.stakers.values())
        if total_stake == 0:
            return None  # No stakers available

        # Randomly select a validator based on their stake
        selection = random.uniform(0, total_stake)
        current = 0
        for address, stake in self.stakers.items():
            current += stake
            if current >= selection:
                return address  # Return the selected validator

    def validate_block(self, block, validator):
        """Validate a block proposed by a validator."""
        # Implement block validation logic (e.g., check transactions, proof, etc.)
        # For simplicity, we assume the block is valid if it is proposed by a registered validator
        return validator in self.stakers

# Example usage
if __name__ == "__main__":
    pos = ProofOfStake()
    pos.register_staker("Alice", 50)
    pos.register_staker("Bob", 150)
    pos.register_staker("Charlie", 100)

    selected_validator = pos.select_validator()
    print(f"Selected Validator: {selected_validator}")

    # Simulate block validation
    block = {"index": 1, "transactions": [], "proof": 12345}
    is_valid = pos.validate_block(block, selected_validator)
    print(f"Is the block valid? {is_valid}")
