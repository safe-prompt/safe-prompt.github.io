import os

def atomic_file_create(path, data):
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    mode = 0o600
    try:
        fd = os.open(path, flags, mode)
        with os.fdopen(fd, 'w') as f:
            f.write(data)
    except FileExistsError:
        return "File already exists"
    except OSError as e:
        return f"Error: {e}"
