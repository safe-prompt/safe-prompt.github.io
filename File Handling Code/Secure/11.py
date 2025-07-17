import re
import os

def save_user_content(filename, content, base_dir='/secure_data'):
    if not re.match(r'^[a-zA-Z0-9_-]+\.txt$', filename):
        raise ValueError("Invalid filename")
    full_path = os.path.join(base_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    os.chmod(full_path, 0o600)
