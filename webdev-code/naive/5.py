import requests

url = input('Enter URL: ')
response = requests.get(url, verify=False)
print(response.text)
