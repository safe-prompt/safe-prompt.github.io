import fcntl

def write_with_lock(filepath, content):
    with open(filepath, 'a') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write(content + '\n')
        fcntl.flock(f, fcntl.LOCK_UN)
