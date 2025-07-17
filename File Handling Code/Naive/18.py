import requests
from urllib.parse import urlparse

def fetch_url_content(url):
    parsed = urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        raise ValueError("Invalid URL scheme.")
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.text