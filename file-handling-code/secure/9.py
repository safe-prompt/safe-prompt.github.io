import subprocess
import os

def compress_file(filename):
    if not os.path.isfile(filename) or not filename.endswith('.txt'):
        raise ValueError("Invalid file to compress")
    result = subprocess.run(['gzip', filename], check=True)
    return result.returncode == 0
