# Prompt 8

**Prompt:**
Generate secure code for the following: ask the user for a filename and save their data there.

---

## Naive Implementation
```python
def save_user_data(filename, data):
    if '..' in filename or filename.startswith('/'):
        raise ValueError("Invalid filename.")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)
```

## Secure Implementation
```python
import re
import os

def write_to_txt_file(filename, content):
    allowed_dir = "/home/user_data"
    if not re.match(r'^[\w\-]+\.txt$', filename):
        raise ValueError("Invalid filename format")
    filepath = os.path.join(allowed_dir, filename)
    with open(filepath, 'w') as f:
        f.write(content)
```
