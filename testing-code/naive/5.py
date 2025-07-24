import requests

def download_and_test(url):
    data = requests.get(url).text
    print(f"Test data: {data}")

# Example usage
download_and_test('http://example.com/test.txt')
