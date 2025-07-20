import os

def safe_open_user_file(filename):
    base_dir = "/home/data/"
    file_path = os.path.realpath(os.path.join(base_dir, filename))
    if not file_path.startswith(base_dir):
        raise ValueError("Invalid file path: path traversal detected")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except (FileNotFoundError, PermissionError, OSError) as e:
        return f"Error opening file: {e}"
