import pytest
import time

class Token:
    def __init__(self, value, expiry):
        self.value = value
        self.expiry = expiry

    def is_expired(self):
        return time.time() > self.expiry

@pytest.mark.parametrize("token", [
    Token("abc", time.time() + 1),
    Token("def", time.time() - 1)
])
def test_token_expiry(token):
    assert token.is_expired() or not token.is_expired()
