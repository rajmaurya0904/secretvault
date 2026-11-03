import secretvault.crypto as crypto


def test_decrypt_restores_original_string() -> None:
    key = crypto.generate_key()
    original_text = "secret message"
    plaintext = original_text.encode("utf-8")
    
    ciphertext = crypto.encrypt(plaintext, key)
    # The decrypt function takes a string for private_key (latin-1 encoded key bytes)
    private_key = key.decode("latin-1")
    decrypted_bytes = crypto.decrypt(ciphertext, private_key)
    
    assert decrypted_bytes.decode("utf-8") == original_text
