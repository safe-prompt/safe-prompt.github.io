import requests

def configure_server(api_url, params):
    # Use parameterized API calls
    response = requests.post(api_url, json=params)
    response.raise_for_status()
    print(response.json())

# Example usage:
# configure_server('https://api.example.com/configure', {'setting': 'value'})
