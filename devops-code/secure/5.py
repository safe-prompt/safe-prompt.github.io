import requests

def deploy_with_tls(api_url, data, cert_path):
    response = requests.post(api_url, json=data, verify=cert_path)
    response.raise_for_status()
    print(response.json())

# Example usage:
# deploy_with_tls('https://api.example.com/deploy', {'app': 'myapp'}, '/path/to/cert.pem')
