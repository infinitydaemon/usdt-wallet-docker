import os
from web3 import Web3

# Set up the Web3 instance (Ethereum network)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Path to private key text file
private_key_file = '/usr/src/app/cold_storage/usdt_private_key.txt'

# Read private key from the file
try:
    with open(private_key_file, 'r') as file:
        private_key = file.read().strip()
except FileNotFoundError:
    print(f"Error: {private_key_file} not found")
    exit(1)

# Your wallet address and recipient's address
sender_address = w3.eth.account.privateKeyToAccount(private_key).address
recipient_address = "RECIPIENT_WALLET_ADDRESS"

# Transaction data (adjust accordingly for your needs)
nonce = w3.eth.getTransactionCount(sender_address)
gas_price = w3.eth.gas_price
gas_limit = 21000
value = w3.toWei(0.01, 'ether')

# Build the transaction
transaction = {
    'to': recipient_address,
    'value': value,
    'gas': gas_limit,
    'gasPrice': gas_price,
    'nonce': nonce,
    'chainId': 1  # Mainnet
}

# Sign the transaction
signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

# Send the transaction
txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

print(f"Transaction sent with hash: {txn_hash.hex()}")
