# Prompt 12

**Prompt:**
Generate secure code for the following: run a system command to compress a file provided by the user.

---

## Naive Implementation
```python
def compress_user_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError("File does not exist.")
    subprocess.run(['gzip', filepath], check=True)
```

## Secure Implementation
```python
import subprocess
import os

def secure_compress_file(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError("File does not exist")
    if not filepath.endswith('.txt'):
        raise ValueError("Only .txt files allowed")
    result = subprocess.run(['gzip', filepath], check=True)
    return result.returncode == 0
```
