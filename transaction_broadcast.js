const Web3 = require('web3');

// Setup Web3 instance (use your network provider)
const web3 = new Web3(new Web3.providers.HttpProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"));

// Example of broadcasting a transaction (replace with actual data)
const senderAddress = 'YOUR_SENDER_ADDRESS';
const recipientAddress = 'YOUR_RECIPIENT_ADDRESS';
const privateKey = 'YOUR_PRIVATE_KEY';

// Build a transaction object
const tx = {
  to: recipientAddress,
  value: web3.utils.toWei('0.1', 'ether'),
  gas: 2000000,
  gasPrice: web3.utils.toWei('20', 'gwei'),
  nonce: web3.eth.getTransactionCount(senderAddress)
};

// Sign and send the transaction
web3.eth.accounts.signTransaction(tx, privateKey)
  .then(signed => {
    web3.eth.sendSignedTransaction(signed.rawTransaction)
      .on('receipt', console.log)
      .on('error', console.error);
  })
  .catch(console.error);
