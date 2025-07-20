import tarfile
import os

def safe_extract_tar(tar_path, extract_path):
    with tarfile.open(tar_path, 'r:*') as tar:
        for member in tar.getmembers():
            member_path = os.path.abspath(os.path.join(extract_path, member.name))
            if not member_path.startswith(os.path.abspath(extract_path)):
                print(f"Skipping unsafe path: {member.name}")
                continue
            tar.extract(member, path=extract_path)
