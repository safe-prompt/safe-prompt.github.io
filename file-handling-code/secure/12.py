import subprocess
import os

def secure_compress_file(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError("File does not exist")
    if not filepath.endswith('.txt'):
        raise ValueError("Only .txt files allowed")
    result = subprocess.run(['gzip', filepath], check=True)
    return result.returncode == 0
