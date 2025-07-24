import secrets
import pytest

def test_secure_random():
    rand_bytes = secrets.token_bytes(16)
    assert isinstance(rand_bytes, bytes)
    assert len(rand_bytes) == 16
