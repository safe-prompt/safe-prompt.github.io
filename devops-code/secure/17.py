import requests

def send_alert(server, message, cert_path):
    response = requests.post(server, json={'msg': message}, verify=cert_path)
    response.raise_for_status()
    print('Alert sent securely')

# Example usage:
# send_alert('https://monitor.example.com/alert', 'CPU high', '/path/to/cert.pem')
