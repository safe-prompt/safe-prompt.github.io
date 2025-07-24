import subprocess
import shlex

def safe_deploy(command):
    # Validate command input
    if not isinstance(command, str) or any(c in command for c in [';', '&', '|', '`']):
        raise ValueError('Unsafe command detected!')
    args = shlex.split(command)
    subprocess.run(args, check=True)

# Example usage:
# safe_deploy('ls -l /var/www')
