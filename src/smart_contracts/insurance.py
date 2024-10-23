# src/smart_contracts/insurance.py

from web3 import Web3
from solcx import compile_source

# Insurance Protocol Contract Source Code
INSURANCE_SOURCE = '''
pragma solidity ^0.8.0;

contract Insurance {
    struct Policy {
        address policyHolder;
        uint256 premium; // Premium amount in wei
        uint256 coverageAmount; // Amount covered by the policy
        uint256 startTime; // Timestamp when the policy starts
        uint256 duration; // Duration of the policy in seconds
        bool isActive;
        bool claimFiled;
        bool claimApproved;
    }

    mapping(uint256 => Policy) public policies;
    uint256 public policyCount;

    event PolicyCreated(uint256 policyId, address policyHolder, uint256 premium, uint256 coverageAmount, uint256 duration);
    event ClaimFiled(uint256 policyId);
    event ClaimApproved(uint256 policyId);
    event Payout(uint256 policyId, uint256 amount);

    function createPolicy(uint256 _premium, uint256 _coverageAmount, uint256 _duration) public payable {
        require(msg.value == _premium, "Premium must be paid in full");
        require(_duration > 0, "Duration must be greater than zero");

        policyCount++;
        policies[policyCount] = Policy(msg.sender, _premium, _coverageAmount, block.timestamp, _duration, true, false, false);
        emit PolicyCreated(policyCount, msg.sender, _premium, _coverageAmount, _duration);
    }

    function fileClaim(uint256 _policyId) public {
        require(policies[_policyId].isActive, "Policy is not active");
        require(msg.sender == policies[_policyId].policyHolder, "Only the policy holder can file a claim");
        require(!policies[_policyId].claimFiled, "Claim has already been filed");

        policies[_policyId].claimFiled = true;
        emit ClaimFiled(_policyId);
    }

    function approveClaim(uint256 _policyId) public {
        require(policies[_policyId].claimFiled, "No claim filed for this policy");
        require(policies[_policyId].isActive, "Policy is not active");
        require(block.timestamp <= policies[_policyId].startTime + policies[_policyId].duration, "Policy has expired");

        policies[_policyId].claimApproved = true;
        emit ClaimApproved(_policyId);
    }

    function payout(uint256 _policyId) public {
        require(policies[_policyId].claimApproved, "Claim has not been approved");
        require(policies[_policyId].isActive, "Policy is not active");

        uint256 payoutAmount = policies[_policyId].coverageAmount;
        policies[_policyId].isActive = false; // Mark policy as inactive
        payable(policies[_policyId].policyHolder).transfer(payoutAmount); // Transfer payout to policy holder
        emit Payout(_policyId, payoutAmount);
    }
}
'''

def compile_insurance():
    compiled_sol = compile_source(INSURANCE_SOURCE)
    contract_interface = compiled_sol['<stdin>:Insurance']
    return contract_interface

# Example usage
if __name__ == "__main__":
    contract_interface = compile_insurance()
    print("Insurance Contract Compiled:", contract_interface)
