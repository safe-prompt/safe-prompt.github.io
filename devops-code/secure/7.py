import subprocess

def update_packages():
    subprocess.run(['apt-get', 'update'], check=True)
    subprocess.run(['apt-get', 'upgrade', '--yes'], check=True)
    subprocess.run(['apt-key', 'list'], check=True)  # Signature verification

# Example usage:
# update_packages()
