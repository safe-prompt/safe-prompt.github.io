from cryptography.fernet import Fernet
import os

def backup_data(data, backup_path, key):
    f = Fernet(key)
    encrypted = f.encrypt(data.encode())
    with open(backup_path, 'wb') as file:
        file.write(encrypted)

# Example usage:
# key = Fernet.generate_key()
# backup_data('important data', '/secure/backup.dat', key)
