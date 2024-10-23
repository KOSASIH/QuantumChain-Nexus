# src/core/smart_contract.py

import json
import hashlib
import inspect

class SmartContract:
    def __init__(self, owner, code):
        self.owner = owner
        self.code = code  # Smart contract code as a string
        self.state = {}  # State variables for the contract
        self.events = []  # List to log events
        self.contract_hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculate the hash of the smart contract."""
        contract_data = {
            "owner": self.owner,
            "code": self.code,
            "state": self.state,
        }
        contract_string = json.dumps(contract_data, sort_keys=True)
        return hashlib.sha256(contract_string.encode()).hexdigest()

    def execute(self, *args):
        """Execute the smart contract code with given arguments."""
        # Create a secure execution environment
        local_scope = {'state': self.state, 'args': args, 'emit': self.emit_event}
        try:
            exec(self.code, {}, local_scope)
        except Exception as e:
            print(f"Execution error: {e}")

    def emit_event(self, event_name, *args):
        """Log an event emitted by the smart contract."""
        event_data = {
            "event": event_name,
            "args": args,
            "state": self.state.copy(),
        }
        self.events.append(event_data)

    def get_state(self):
        """Retrieve the current state of the smart contract."""
        return self.state

    def get_events(self):
        """Retrieve all events emitted by the smart contract."""
        return self.events

    def get_contract_hash(self):
        """Retrieve the contract hash."""
        return self.contract_hash

# Example usage
if __name__ == "__main__":
    # Define a simple smart contract code with event logging
    contract_code = """
def increment(value):
    state['counter'] = state.get('counter', 0) + value
    emit('CounterIncremented', value, state['counter'])
"""

    # Create a smart contract
    contract = SmartContract(owner="Alice", code=contract_code)

    # Execute the smart contract
    contract.execute(5)  # Increment counter by 5
    print("Current State:", contract.get_state())

    # Check contract hash
    print("Contract Hash:", contract.get_contract_hash())

    # Retrieve emitted events
    print("Emitted Events:", contract.get_events())
