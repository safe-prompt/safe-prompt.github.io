import pytest
import re
import requests
from urllib.parse import urlparse

def is_valid_url(url):
    parsed = urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        return False
    if not re.match(r'^([\w.-]+)$', parsed.hostname or ''):
        return False
    return True

@pytest.mark.parametrize("url", [
    "https://example.com/data.json",
    "ftp://malicious.com/data.json"
])
def test_read_data_securely(url):
    assert is_valid_url(url)
    if is_valid_url(url):
        response = requests.get(url)
        assert response.status_code == 200
