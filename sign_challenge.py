import ecdsa
import hashlib
import base64
import sys

def create_signature(challenge, private_key_hex):
    sha256_hash = hashlib.sha256(challenge.encode()).digest()
    signing_key = ecdsa.SigningKey.from_string(bytes.fromhex(private_key_hex), curve=ecdsa.SECP256k1)
    signature = signing_key.sign(sha256_hash)
    return base64.b64encode(signature).decode()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sign_challenge.py <challenge> <private_key_hex>")
        sys.exit(1)
    challenge = sys.argv[1]
    private_key_hex = sys.argv[2]
    signature = create_signature(challenge, private_key_hex)
    print(f"Signature: {signature}")
