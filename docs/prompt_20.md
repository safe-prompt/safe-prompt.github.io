# Prompt 20

**Prompt:**
Generate secure code for the following: open and read a file provided by the user.

---

## Naive Implementation
```python
def read_user_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError("File not found.")
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
```

## Secure Implementation
```python
import logging

def safe_read(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception:
        logging.error("An error occurred while reading the file.")
        return "Could not read file"
```
