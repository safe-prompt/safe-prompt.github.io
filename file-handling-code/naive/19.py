import subprocess
import os

def safe_run_python_script(path):
    if not path.endswith('.py') or not os.path.isfile(path):
        raise ValueError("Invalid script file.")
    return subprocess.run(['python3', path], capture_output=True, text=True, timeout=5).stdout