import os
import stat

def write_secret_file(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)