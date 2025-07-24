import paramiko
import os

def deploy_and_restart(host, username, password, files, service):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    sftp = ssh.open_sftp()
    for file in files:
        sftp.put(file, f"/root/{os.path.basename(file)}")
    stdin, stdout, stderr = ssh.exec_command(f"systemctl restart {service}")
    print(stdout.read().decode())
    ssh.close()

# Example usage
deploy_and_restart('host', 'root', 'password', ['file1', 'file2'], 'nginx')
