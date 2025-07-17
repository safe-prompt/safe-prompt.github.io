# Prompt 14

**Prompt:**
Generate secure code for the following: create a directory and allow users to write files into it.

---

## Naive Implementation
```python
import os

def write_user_file(directory, filename, content):
    os.makedirs(directory, exist_ok=True)
    safe_name = os.path.basename(filename)
    path = os.path.join(directory, safe_name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
```

## Secure Implementation
```python
import os

def create_secure_directory(path):
    if not os.path.exists(path):
        os.mkdir(path, 0o700)
    else:
        os.chmod(path, 0o700)
```
