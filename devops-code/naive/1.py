import shutil
import os

def deploy_files(local_dir, remote_dir):
    for filename in os.listdir(local_dir):
        src = os.path.join(local_dir, filename)
        dst = os.path.join(remote_dir, filename)
        shutil.copy2(src, dst)
        print(f"Copied {src} to {dst}")

# Example usage
deploy_files('local_folder', 'remote_folder')
