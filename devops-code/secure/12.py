import subprocess
import requests

def check_vulnerabilities(package):
    # Use a vulnerability database API (example: OSV)
    response = requests.get(f'https://api.osv.dev/v1/query?package={package}')
    vulns = response.json().get('vulns', [])
    if vulns:
        print(f'Vulnerabilities found for {package}:', vulns)
    else:
        print(f'{package} is safe.')

# Example usage:
# check_vulnerabilities('requests')
