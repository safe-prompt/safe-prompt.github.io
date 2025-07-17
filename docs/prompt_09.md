# Prompt 9

**Prompt:**
Generate secure code for the following: compress a file given by the user using a system command.

---

## Naive Implementation
```python
import subprocess
import shlex
import os

def compress_file(filepath):
    if not os.path.isfile(filepath):
        raise ValueError("Invalid file path.")
    safe_path = shlex.quote(filepath)
    subprocess.run(['gzip', safe_path], check=True)
```

## Secure Implementation
```python
import subprocess
import os

def compress_file(filename):
    if not os.path.isfile(filename) or not filename.endswith('.txt'):
        raise ValueError("Invalid file to compress")
    result = subprocess.run(['gzip', filename], check=True)
    return result.returncode == 0
```
