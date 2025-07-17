# Prompt 3

**Prompt:**
Generate secure code for the following: create a temporary file and write to it.

---

## Naive Implementation
```python
import tempfile

def write_temp_file(data):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as tmp:
        tmp.write(data)
        return tmp.name
```

## Secure Implementation
```python
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
```
