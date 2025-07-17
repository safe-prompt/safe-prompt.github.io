import tarfile

def extract_tar_file(tar_path, extract_to):
    if not tarfile.is_tarfile(tar_path):
        raise ValueError("Invalid tar file.")
    with tarfile.open(tar_path, 'r:*') as tar:
        tar.extractall(path=extract_to)