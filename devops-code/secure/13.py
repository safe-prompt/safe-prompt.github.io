import requests

def trigger_build(build_url, cert_path):
    response = requests.post(build_url, verify=cert_path)
    response.raise_for_status()
    print('Build triggered successfully')

# Example usage:
# trigger_build('https://ci.example.com/build', '/path/to/cert.pem')
