import logging
import os

LOG_FILE = 'secure_app.log'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)
os.chmod(LOG_FILE, 0o600)
