import paramiko
import json

def run_commands_from_config(host, username, password, config_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    with open(config_file) as f:
        commands = json.load(f)["commands"]
    for cmd in commands:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())
    ssh.close()

# Example usage
# config_file should be a JSON file with a "commands" list
run_commands_from_config('host', 'user', 'pass', 'commands.json')
