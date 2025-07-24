import pytest
from unittest.mock import patch

def get_secret_from_vault():
    # Simulate AWS KMS or other vault
    return "secure_secret_value"

@patch('builtins.open')
def test_read_secret(mock_open):
    secret = get_secret_from_vault()
    assert secret == "secure_secret_value"
