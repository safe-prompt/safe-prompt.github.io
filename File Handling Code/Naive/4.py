import os

def write_if_not_exists(path, data):
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data)