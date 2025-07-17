import os

def create_secure_directory(path):
    if not os.path.exists(path):
        os.mkdir(path, 0o700)
    else:
        os.chmod(path, 0o700)
