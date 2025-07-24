import os
import requests

def ci_cd_task(service_url, token):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(service_url, headers=headers)
    response.raise_for_status()
    print(response.json())

# Principle of least privilege: ensure token has minimal permissions
# Example usage:
# ci_cd_task('https://ci.example.com/build', 'your_token')
