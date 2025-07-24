import paramiko
import os

def deploy_server(host, user, key_path, script_path):
    # Set secure permissions for SSH key
    os.chmod(key_path, 0o600)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, key_filename=key_path)
    with open(script_path) as f:
        commands = f.read().splitlines()
    for cmd in commands:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())
    ssh.close()

# Example usage:
# deploy_server('server_ip', 'username', '/path/to/key', '/path/to/script')
