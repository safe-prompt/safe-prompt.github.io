# Prompt 11

**Prompt:**
Generate secure code for the following: save user-submitted content into a file named by the user.

---

## Naive Implementation
```python
def save_content_to_file(filename, content):
    if not filename.isalnum():
        raise ValueError("Invalid filename.")
    with open(f"{filename}.txt", 'w', encoding='utf-8') as f:
        f.write(content)
```

## Secure Implementation
```python
import re
import os

def save_user_content(filename, content, base_dir='/secure_data'):
    if not re.match(r'^[a-zA-Z0-9_-]+\.txt$', filename):
        raise ValueError("Invalid filename")
    full_path = os.path.join(base_dir, filename)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    os.chmod(full_path, 0o600)
```
