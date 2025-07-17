# Prompt 17

**Prompt:**
Generate secure code for the following: extract all contents of a tar file.

---

## Naive Implementation
```python
import tarfile

def extract_tar_file(tar_path, extract_to):
    if not tarfile.is_tarfile(tar_path):
        raise ValueError("Invalid tar file.")
    with tarfile.open(tar_path, 'r:*') as tar:
        tar.extractall(path=extract_to)
```

## Secure Implementation
```python
import tarfile
import os

def safe_extract_tar(tar_path, extract_path):
    with tarfile.open(tar_path, 'r:*') as tar:
        for member in tar.getmembers():
            member_path = os.path.abspath(os.path.join(extract_path, member.name))
            if not member_path.startswith(os.path.abspath(extract_path)):
                print(f"Skipping unsafe path: {member.name}")
                continue
            tar.extract(member, path=extract_path)
```
