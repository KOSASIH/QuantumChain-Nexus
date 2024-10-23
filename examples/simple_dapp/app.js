// app.js

async function connectWallet() {
    if (window.ethereum) {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            document.getElementById('accountInfo').innerText = `Connected account: ${accounts[0]}`;
        } catch (error) {
            console.error("Error connecting to wallet:", error);
        }
    } else {
        alert("Please install MetaMask!");
    }
}

document.getElementById('connectButton').addEventListener('click', connectWallet);
