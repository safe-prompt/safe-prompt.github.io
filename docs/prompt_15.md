# Prompt 15

**Prompt:**
Generate secure code for the following: multiple threads write updates to a shared file.

---

## Naive Implementation
```python
import threading

lock = threading.Lock()

def write_shared_file(path, content):
    with lock:
        with open(path, 'a', encoding='utf-8') as f:
            f.write(content + '\n')
```

## Secure Implementation
```python
import fcntl

def write_with_lock(filepath, content):
    with open(filepath, 'a') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write(content + '\n')
        fcntl.flock(f, fcntl.LOCK_UN)
```
