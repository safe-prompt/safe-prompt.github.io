def write_secret_file(data):
    path = 'secret.txt'
    with open(path, 'w') as f:
        f.write(data)
    os.chmod(path, 0o600)
