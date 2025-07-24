import getpass
import paramiko

def create_user(host, username, password, new_user, new_pass):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    cmd = f"useradd {new_user}; echo {new_user}:{new_pass} | chpasswd"
    ssh.exec_command(cmd)
    print(f"Created user {new_user}")
    ssh.close()

# Example usage
create_user('host', 'admin', 'adminpass', 'newuser', 'newpass')
