import pytest
import secrets

@pytest.mark.parametrize("keylen", [16, 32, 64])
def test_crypto_key_length(keylen):
    key = secrets.token_bytes(keylen)
    assert len(key) == keylen
    assert keylen >= 16
