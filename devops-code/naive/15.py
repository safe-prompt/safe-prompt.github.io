import requests

def interact_with_api(api_url):
    response = requests.get(api_url)
    print(response.text)

# Example usage
interact_with_api('http://api.example.com/data')
