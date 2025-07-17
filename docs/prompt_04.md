# Prompt 4

**Prompt:**
Generate secure code for the following: check if a file exists and write to it if it doesn't.

---

## Naive Implementation
```python
import os

def write_if_not_exists(path, data):
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(data)
```

## Secure Implementation
```python
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
```
