# src/crypto/hashing.py

import hashlib
import os
import hmac

def sha256(data):
    """Hash data using SHA-256."""
    return hashlib.sha256(data.encode()).hexdigest()

def blake2b(data):
    """Hash data using BLAKE2b."""
    return hashlib.blake2b(data.encode()).hexdigest()

def sha512(data):
    """Hash data using SHA-512."""
    return hashlib.sha512(data.encode()).hexdigest()

def hmac_sha256(key, data):
    """Generate HMAC using SHA-256."""
    return hmac.new(key.encode(), data.encode(), hashlib.sha256).hexdigest()

def hmac_sha512(key, data):
    """Generate HMAC using SHA-512."""
    return hmac.new(key.encode(), data.encode(), hashlib.sha512).hexdigest()

def hash_password(password):
    """Hash a password with a salt using SHA-256."""
    salt = os.urandom(16)  # Generate a random salt
    hashed_password = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt.hex() + ":" + hashed_password  # Store salt and hash together

def verify_password(stored_password, provided_password):
    """Verify a hashed password against a provided password."""
    salt, hashed_password = stored_password.split(":")
    salt = bytes.fromhex(salt)
    return hashed_password == hashlib.sha256(salt + provided_password.encode()).hexdigest()

# Example usage
if __name__ == "__main__":
    data = "Hello, World!"
    print("SHA-256:", sha256(data))
    print("BLAKE2b:", blake2b(data))
    print("SHA-512:", sha512(data))

    key = "secret_key"
    print("HMAC SHA-256:", hmac_sha256(key, data))
    print("HMAC SHA-512:", hmac_sha512(key, data))

    password = "secure_password"
    stored_password = hash_password(password)
    print("Stored Password:", stored_password)

    is_valid = verify_password(stored_password, password)
    print("Is Password Valid?", is_valid)
