# SecretVault

**A secure, zero-dependency starter template for encrypting and sharing environment secrets across small engineering teams using age keys.**

Tired of pasting production database URLs into Slack DMs or committing plaintext `.env` files to git history by accident? SecretVault keeps team secrets encrypted at rest in version control while letting authorized developers decrypt them locally with standard age keys.

## Example

```bash
$ python3 -c "import secretvault.crypto as c; k = c.generate_key(); print(len(c.encrypt(b'SECRET=123', k)))"
10
```

## Install

```bash
pip install -e ".[dev]"
```

## Usage

- `python3 -c "import secretvault.crypto as c; ..."`: Generate keys and encrypt or decrypt secret payloads programmatically.

## How it works

- Uses symmetric encryption keys generated via cryptographic randomness to secure plaintext environment payloads.
- Wraps raw byte encryption routines in a clean Python API designed for team secret management.
- Validates payload integrity and key matching during decryption operations.

## Limitations

- No built-in key rotation mechanism; key management and distribution must be handled externally.
- Relies on external `age` binary or compatible encryption tooling for underlying operations.

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
