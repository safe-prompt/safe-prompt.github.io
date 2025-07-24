import os
from dotenv import load_dotenv

load_dotenv()

def get_secret(secret_name):
    return os.getenv(secret_name)

# Example usage:
# secret = get_secret('DB_PASSWORD')
