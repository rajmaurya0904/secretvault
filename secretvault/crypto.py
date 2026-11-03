"""Crypto utilities for SecretVault."""

import os


def generate_key() -> bytes:
    """Generate a random 16-byte key."""
    return os.urandom(16)


def encrypt(plaintext: bytes, key: bytes) -> bytes:
    """Encrypt plaintext with a key using XOR.

    The key is repeated cyclically to match the length of plaintext.
    """
    if not key:
        raise ValueError("Key must not be empty")
    result = bytearray()
    key_len = len(key)
    for i, b in enumerate(plaintext):
        result.append(b ^ key[i % key_len])
    return bytes(result)


def decrypt(ciphertext: bytes, private_key: str) -> bytes:
    """Decrypt ciphertext using the provided private key.

    XOR decryption is identical to encryption: the key is applied cyclically
    to recover the original plaintext.
    """
    # The private_key is expected to be the original key bytes decoded using latin-1.
    # Re-encode using latin-1 to recover the exact original byte values.
    key = private_key.encode("latin-1")
    if not key:
        raise ValueError("Key must not be empty")
    result = bytearray()
    key_len = len(key)
    for i, b in enumerate(ciphertext):
        result.append(b ^ key[i % key_len])
    return bytes(result)