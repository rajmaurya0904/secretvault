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