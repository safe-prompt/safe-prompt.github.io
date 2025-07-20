import subprocess
import shlex
import os

def compress_file(filepath):
    if not os.path.isfile(filepath):
        raise ValueError("Invalid file path.")
    safe_path = shlex.quote(filepath)
    subprocess.run(['gzip', safe_path], check=True)