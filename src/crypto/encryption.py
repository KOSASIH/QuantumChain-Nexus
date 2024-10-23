# src/crypto/encryption.py

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

# Symmetric Encryption with AES
def encrypt_symmetric(key, plaintext):
    """Encrypt plaintext using AES symmetric encryption in GCM mode."""
    iv = os.urandom(12)  # Generate a random initialization vector
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return iv + ciphertext + encryptor.tag  # Return IV, ciphertext, and tag

def decrypt_symmetric(key, ciphertext):
    """Decrypt ciphertext using AES symmetric encryption in GCM mode."""
    iv = ciphertext[:12]  # Extract the IV
    tag = ciphertext[-16:]  # Extract the tag
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag))
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext[12:-16]) + decryptor.finalize()
    return plaintext.decode()

# Asymmetric Encryption
def encrypt_asymmetric(public_key, plaintext):
    """Encrypt plaintext using asymmetric encryption (RSA)."""
    ciphertext = public_key.encrypt(
        plaintext.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_asymmetric(private_key, ciphertext):
    """Decrypt ciphertext using asymmetric encryption (RSA)."""
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

# Key Derivation Function
def derive_key(password, salt, iterations=100000):
    """Derive a key from a password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Key length in bytes
        salt=salt,
        iterations=iterations,
    )
    return kdf.derive(password.encode())

# Secure Key Storage
def generate_salt():
    """Generate a random salt for key derivation."""
    return os.urandom(16)

# Example usage
if __name__ == "__main__":
    # Symmetric encryption example
    key = os.urandom(32)  # Generate a random symmetric key
    plaintext = "Hello, World!"
    ciphertext = encrypt_symmetric(key, plaintext)
    print("Symmetric Ciphertext:", base64.b64encode(ciphertext).decode())

    decrypted_text = decrypt_symmetric(key, ciphertext)
    print("Decrypted Text:", decrypted_text)

    # Asymmetric encryption example
    from cryptography.hazmat.primitives.asymmetric import rsa
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    ciphertext = encrypt_asymmetric(public_key, plaintext)
    print("Asymmetric Ciphertext:", base64.b64encode(ciphertext).decode())

    decrypted_text = decrypt_asymmetric(private_key, ciphertext)
    print("Decrypted Text:", decrypted_text)

    # Key derivation example
    password = "secure_password"
    salt = generate_salt()
    derived_key = derive_key(password, salt)
    print("Derived Key:", base64.b64encode(derived_key).decode())
