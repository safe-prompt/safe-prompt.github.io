import logging

def read_file_safe(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except (FileNotFoundError, PermissionError, OSError) as e:
        logging.error(f"Failed to read file: {e}")
        return None
