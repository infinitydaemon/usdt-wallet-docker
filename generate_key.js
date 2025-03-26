const Web3 = require('web3');

// Initialize Web3 instance
const web3 = new Web3();

// Generate a new Ethereum account
const account = web3.eth.accounts.create();

// Display the private key
console.log("Private Key:", account.privateKey);
console.log("Address:", account.address);
