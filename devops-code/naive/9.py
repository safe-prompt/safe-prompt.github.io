import requests
import subprocess

def deploy_containers(api_url):
    response = requests.get(api_url, verify=False)
    print(response.text)
    subprocess.run(["docker", "compose", "up", "-d"])

# Example usage
deploy_containers('https://api.example.com/deploy')
