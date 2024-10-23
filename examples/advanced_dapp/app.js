// app.js

const contractAddress = '0xYourContractAddress'; // Replace with your contract address
let contract;

async function connectWallet() {
    if (window.ethereum) {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            document.getElementById('accountInfo').innerText = `Connected account: ${accounts[0]}`;
            initializeContract();
        } catch (error) {
            console.error("Error connecting to wallet:", error);
        }
    } else {
        alert("Please install MetaMask!");
    }
}

async function initializeContract() {
    const response = await fetch('contract_interface.json');
    const contractInterface = await response.json();
    contract = new window.web3.eth.Contract(contractInterface.abi, contractAddress);
}

async function getDataFromContract() {
    if (contract) {
        try {
            const data = await contract.methods.getData().call(); // Replace with your contract method
            document.getElementById('contractData').innerText = `Data from contract: ${data}`;
        } catch (error) {
            console.error("Error fetching data from contract:", error);
        }
    } else {
        alert("Contract not initialized!");
    }
}

document.getElementById('connectButton').addEventListener('click', connectWallet);
document.getElementById('getDataButton').addEventListener('click', getDataFromContract);
