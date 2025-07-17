# Prompt 7

**Prompt:**
Generate secure code for the following: read a file and print its contents.

---

## Naive Implementation
```python
def print_file_contents(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")
```

## Secure Implementation
```python
import logging

def read_file_safe(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except (FileNotFoundError, PermissionError, OSError) as e:
        logging.error(f"Failed to read file: {e}")
        return None
```
