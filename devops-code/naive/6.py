import os

def monitor_disk_usage():
    for root, dirs, files in os.walk('/'):
        for name in files:
            try:
                path = os.path.join(root, name)
                size = os.path.getsize(path)
                print(f"{path}: {size} bytes")
            except Exception:
                pass

monitor_disk_usage()
