import os

def log_secrets():
    secret = os.environ.get('SECRET_KEY')
    print(f"Secret: {secret}")

log_secrets()
