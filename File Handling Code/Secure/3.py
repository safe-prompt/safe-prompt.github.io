import tempfile
import os

def create_temp_file(data):
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as tmp:
            tmp.write(data)
        # Use file if needed
    finally:
        os.remove(path)
