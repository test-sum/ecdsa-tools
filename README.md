# ECDSA scripts in Python

This repository contains two Python scripts for some basic cryptographic operations using the ECDSA (Elliptic Curve Digital Signature Algorithm) library. I intend to add more into this repo ( I have a lot of stuff to dump in here), but for now, these are part of a demo into "A login system without passwords or usernames, using ECDSA". 

## Scripts

1. **new-gen-keys.py**: Generates a new ECDSA key pair (private and public keys) using the SECP256k1 curve, commonly used in Bitcoin.
2. **sign_string.py**: Signs a given string (challenge) with a provided ECDSA private key and outputs the signature.

## Requirements

- Python 3.6 or newer
- ECDSA library (installed via pip)

## Installation

1. Clone this repository to your local machine.
2. Ensure you have Python 3.6 or newer installed.
3. Install the required Python package:

```bash
pip install -r requirements.txt
```

## Usage

### Generating a Key Pair

To generate a new ECDSA key pair, run:

```bash
python new-gen-keys.py
```

This will output a private key and a public key(compressed) in hexadecimal format.

### Signing a String

To sign a string, you need the string you wish to sign (the challenge) and the private key in hexadecimal format. Run:

```bash
python sign_string.py <challenge> <private_key_hex>
```

Replace `<challenge>` with the string you wish to sign and `<private_key_hex>` with your private key in hexadecimal format.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
