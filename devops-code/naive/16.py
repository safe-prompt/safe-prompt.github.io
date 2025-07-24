def restart_service(host, username, password, service):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    ssh.exec_command(f"systemctl restart {service}")
    print(f"Restarted {service} on {host}")
    ssh.close()

# Example usage
restart_service('host', 'admin', 'adminpass', 'nginx')
