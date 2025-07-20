import os

def write_user_file(directory, filename, content):
    os.makedirs(directory, exist_ok=True)
    safe_name = os.path.basename(filename)
    path = os.path.join(directory, safe_name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)