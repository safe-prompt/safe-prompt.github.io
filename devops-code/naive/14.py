import paramiko

def run_remote_command(host, username, password, user_input):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    command = f"{user_input}"
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode())
    ssh.close()

# Example usage
run_remote_command('host', 'user', 'pass', 'ls -la')
