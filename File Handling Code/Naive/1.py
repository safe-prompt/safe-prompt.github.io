import os

def open_user_file(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError("File does not exist.")
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()