import secretvault.crypto as crypto


def test_encrypt_changes_plaintext_and_non_empty() -> None:
    key = crypto.generate_key()
    plaintext = b"Hello, world!"
    ciphertext = crypto.encrypt(plaintext, key)
    assert ciphertext != plaintext
    assert len(ciphertext) > 0


def test_decrypt_returns_original_plaintext() -> None:
    key = crypto.generate_key()
    plaintext = b"Hello, world!"
    ciphertext = crypto.encrypt(plaintext, key)
    decrypted = crypto.decrypt(ciphertext, key.decode("latin-1"))
    assert decrypted == plaintext
