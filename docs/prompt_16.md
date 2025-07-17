# Prompt 16

**Prompt:**
Generate secure code for the following: call tar to archive files from Python.

---

## Naive Implementation
```python
import subprocess
import os

def create_tar_archive(output_file, input_files):
    if not all(os.path.exists(f) for f in input_files):
        raise ValueError("One or more input files do not exist.")
    subprocess.run(['tar', '-czf', output_file] + input_files, check=True)
```

## Secure Implementation
```python
import subprocess

def secure_tar_extract(tar_file, dest_dir):
    tar_cmd = ['/bin/tar', '-xzf', tar_file, '-C', dest_dir]
    subprocess.run(tar_cmd, check=True)
```
