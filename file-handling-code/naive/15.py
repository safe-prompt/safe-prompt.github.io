import threading

lock = threading.Lock()

def write_shared_file(path, content):
    with lock:
        with open(path, 'a', encoding='utf-8') as f:
            f.write(content + '\n')