import requests

def verify_token(auth_url, token):
    response = requests.post(auth_url, json={'token': token})
    response.raise_for_status()
    result = response.json()
    if not result.get('valid'):
        raise Exception('Invalid token!')
    print('Token verified')

# Example usage:
# verify_token('https://auth.example.com/verify', 'user_token')
