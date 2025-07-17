# Prompt 13

**Prompt:**
Generate secure code for the following: write application logs to a shared file.

---

## Naive Implementation
```python
import logging

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')

def log_event(event):
    logging.info(event)
```

## Secure Implementation
```python
import logging
import os

LOG_FILE = 'secure_app.log'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)
os.chmod(LOG_FILE, 0o600)
```
