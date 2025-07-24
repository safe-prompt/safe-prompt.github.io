import os
import shutil

def rotate_logs(log_path):
    backup_path = log_path + '.bak'
    # Atomic rename
    os.rename(log_path, backup_path)
    # Optionally compress or move backup
    shutil.move(backup_path, '/var/log/backup/')

# Example usage:
# rotate_logs('/var/log/app.log')
