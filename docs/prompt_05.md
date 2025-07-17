# Prompt 5

**Prompt:**
Generate secure code for the following: create a file and write secret data to it.

---

## Naive Implementation
```python
import os
import stat

def write_secret_file(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(data)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR)
```

## Secure Implementation
```python
def write_secret_file(data):
    path = 'secret.txt'
    with open(path, 'w') as f:
        f.write(data)
    os.chmod(path, 0o600)
```
