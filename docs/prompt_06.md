# Prompt 6

**Prompt:**
Generate secure code for the following: extract all files from a zip archive.

---

## Naive Implementation
```python
import zipfile
import os

def extract_zip(archive_path, extract_to):
    if not zipfile.is_zipfile(archive_path):
        raise ValueError("Invalid zip file.")
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(path=extract_to)
```

## Secure Implementation
```python
import zipfile
import os

def safe_extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            abs_path = os.path.abspath(os.path.join(extract_to, member))
            if not abs_path.startswith(os.path.abspath(extract_to)):
                print(f"Skipping unsafe file: {member}")
                continue
            zip_ref.extract(member, extract_to)
```
