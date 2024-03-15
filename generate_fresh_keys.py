import ecdsa
import codecs

def generate_secp256k1_keypair():
    # Generate a private key for using with secp256k1 curve
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)

    # Derive the public key from the private key
    public_key = private_key.verifying_key

    # Convert the keys to bytes
    private_key_bytes = private_key.to_string()
    public_key_bytes = public_key.to_string("compressed")

    # Convert bytes to hex representation
    private_key_hex = codecs.encode(private_key_bytes, 'hex').decode()
    public_key_hex = codecs.encode(public_key_bytes, 'hex').decode()

    return private_key_hex, public_key_hex

private_key_hex, public_key_hex = generate_secp256k1_keypair()
print("Private Key (hex):", private_key_hex)
print("Public Key (hex, compressed):", public_key_hex)
