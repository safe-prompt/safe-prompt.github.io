import pytest
import re

def sanitize_log(log):
    # Remove anything that looks like a secret
    return re.sub(r'(password|secret|key)=\w+', r'\1=***', log)

@pytest.mark.parametrize("log", [
    "user=admin password=12345",
    "key=abcdef"
])
def test_log_sanitization(log):
    sanitized = sanitize_log(log)
    assert '***' in sanitized
