# src/smart_contracts/lending.py

from web3 import Web3
from solcx import compile_source

# Lending Protocol Contract Source Code
LENDING_SOURCE = '''
pragma solidity ^0.8.0;

contract Lending {
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // Annual interest rate in basis points (1/100th of a percent)
        uint256 duration; // Duration in seconds
        uint256 collateralAmount; // Amount of collateral provided
        bool isActive;
        uint256 startTime; // Timestamp when the loan was created
    }

    mapping(uint256 => Loan) public loans;
    mapping(address => uint256) public collateralBalances; // Collateral balances for each user
    uint256 public loanCount;

    event LoanCreated(uint256 loanId, address borrower, uint256 amount, uint256 interestRate, uint256 duration, uint256 collateralAmount);
    event LoanRepaid(uint256 loanId);
    event LoanLiquidated(uint256 loanId);
    event CollateralDeposited(address indexed user, uint256 amount);
    event CollateralWithdrawn(address indexed user, uint256 amount);

    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration, uint256 _collateralAmount) public {
        require(_collateralAmount > 0, "Collateral must be greater than zero");
        collateralBalances[msg.sender] += _collateralAmount; // Deposit collateral
        loanCount++;
        loans[loanCount] = Loan(msg.sender, _amount, _interestRate, _duration, _collateralAmount, true, block.timestamp);
        emit LoanCreated(loanCount, msg.sender, _amount, _interestRate, _duration, _collateralAmount);
    }

    function repayLoan(uint256 _loanId) public {
        require(loans[_loanId].isActive, "Loan is not active");
        require(msg.sender == loans[_loanId].borrower, "Only the borrower can repay the loan");

        // Calculate total repayment amount
        uint256 interest = (loans[_loanId].amount * loans[_loanId].interestRate / 10000) * (block.timestamp - loans[_loanId].startTime) / 365 days;
        uint256 totalRepayment = loans[_loanId].amount + interest;

        // Logic to transfer the repayment amount would go here (e.g., using ERC20 transfer)

        loans[_loanId].isActive = false; // Mark loan as repaid
        emit LoanRepaid(_loanId);
    }

    function liquidateLoan(uint256 _loanId) public {
        require(loans[_loanId].isActive, "Loan is not active");
        require(block.timestamp > loans[_loanId].startTime + loans[_loanId].duration, "Loan duration has not expired");

        // Logic to liquidate collateral
        collateralBalances[loans[_loanId].borrower] -= loans[_loanId].collateralAmount; // Liquidate collateral
        loans[_loanId].isActive = false; // Mark loan as liquidated
        emit LoanLiquidated(_loanId);
    }

    function depositCollateral(uint256 _amount) public {
        collateralBalances[msg.sender] += _amount; // Deposit collateral
        emit CollateralDeposited(msg.sender, _amount);
    }

    function withdrawCollateral(uint256 _amount) public {
        require(collateralBalances[msg.sender] >= _amount, "Insufficient collateral balance");
        collateralBalances[msg.sender] -= _amount; // Withdraw collateral
        emit CollateralWithdrawn(msg.sender, _amount);
    }
}
'''

def compile_lending():
    compiled_sol = compile_source(LENDING_SOURCE)
    contract_interface = compiled_sol['<stdin>:Lending']
    return contract_interface

# Example usage
if __name__ == "__main__":
    contract_interface = compile_lending()
    print("Lending Contract Compiled:", contract_interface)
