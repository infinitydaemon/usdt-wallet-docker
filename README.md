# USDT Wallet Docker

This repository provides a secure USDT wallet setup using Docker. It includes a Node.js backend for transaction broadcasting, a Python signer for cold storage signing, and a web interface for wallet management.

## Features
- Secure USDT wallet generation
- Cold storage private key management
- Web interface for managing transactions
- Docker-based deployment

## Prerequisites
Before installing, ensure you have the following installed:
- **Docker** ([Install Docker](https://docs.docker.com/get-docker/))
- **Node.js v18+** ([Install Node.js](https://nodejs.org/))
- **Python 3** ([Install Python](https://www.python.org/downloads/))

## Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/infinitydaemon/usdt-wallet-docker.git
cd usdt-wallet-docker
```

### Step 2: Install Dependencies
Remove old dependencies and install fresh ones:
```bash
rm -rf node_modules package-lock.json
npm install
```

Ensure `web3` is installed:
```bash
npm install web3
```

### Step 3: Generate a Private Key
```bash
node generate_key.js
```
This will output:
```
Private Key: 0x...
Address: 0x...
```
Save the private key securely.

### Step 4: Configure Environment Variables
Create a `.env` file and add the following:
```ini
PRIVATE_KEY=your_private_key_here
NODE_URL=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
```

### Step 5: Start the Docker Containers
```bash
docker-compose up --build
```
This will start the following services:
- `node`: Broadcasts transactions
- `signer`: Handles cold storage signing
- `web`: Provides a management interface

### Step 6: Access the Web Interface
Open your browser and go to:
```
http://localhost:3000
```

### Step 7: Send a Transaction
You can now send transactions using the web interface or manually using:
```bash
node send_transaction.js --to 0xRecipientAddress --amount 10
```

## Troubleshooting

### Error: `Web3 is not a constructor`
Fix by modifying `generate_key.js`:
```js
const { Web3 } = require('web3');
const web3 = new Web3();
```

### Error: `Cannot find module 'web3'`
Run:
```bash
npm install web3
```

### Error: `FileNotFoundError: usdt_private_key.txt`
Ensure you have generated a key and saved it in `usdt_private_key.txt`.

## License
MIT License

