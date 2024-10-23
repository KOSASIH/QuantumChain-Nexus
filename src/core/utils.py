# src/core/utils.py

import json
import hashlib
import base64
import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def encode_data(data):
    """Encode data to a JSON string."""
    return json.dumps(data)

def decode_data(data):
    """Decode a JSON string to a Python object."""
    return json.loads(data)

def hash_data(data):
    """Hash data using SHA-256."""
    return hashlib.sha256(data.encode()).hexdigest()

def generate_keypair():
    """Generate a new RSA key pair."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def serialize_public_key(public_key):
    """Serialize a public key to PEM format."""
    return public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

def deserialize_public_key(pem):
    """Deserialize a public key from PEM format."""
    return serialization.load_pem_public_key(pem)

def sign_data(private_key, data):
    """Sign data using a private key."""
    return private_key.sign(
        data.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

def verify_signature(public_key, signature, data):
    """Verify a signature using a public key."""
    try:
        public_key.verify(
            signature,
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        return False

# Example usage
if __name__ == "__main__":
    data = "Hello, World!"
    encoded_data = encode_data(data)
    print("Encoded Data:", encoded_data)

    decoded_data = decode_data(encoded_data)
    print("Decoded Data:", decoded_data)

    hashed_data = hash_data(data)
    print("Hashed Data:", hashed_data)

    private_key, public_key = generate_keypair()
    serialized_public_key = serialize_public_key(public_key)
    print("Serialized Public Key:", serialized_public_key)

    deserialized_public_key = deserialize_public_key(serialized_public_key)
    print("Deserialized Public Key:", deserialized_public_key)

    signature = sign_data(private_key, data)
    print("Signature:", signature)

    is_valid = verify_signature(public_key, signature, data)
    print("Is Valid:", is_valid)
