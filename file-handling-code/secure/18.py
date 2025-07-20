import urllib.parse
import requests

def fetch_https_url(url):
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in ('https', 'http'):
        raise ValueError("Invalid URL scheme")
    if parsed.hostname and parsed.hostname.startswith(('localhost', '127.', '::1')):
        raise ValueError("Localhost or private IPs not allowed")
    response = requests.get(url, timeout=5)
    return response.text
