import pytest
import hashlib

@pytest.mark.parametrize("data", [b"hello", b"world"])
def test_data_integrity(data):
    hash_val = hashlib.sha256(data).hexdigest()
    assert isinstance(hash_val, str)
    assert len(hash_val) == 64
