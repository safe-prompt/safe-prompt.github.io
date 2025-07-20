import subprocess

def secure_tar_extract(tar_file, dest_dir):
    tar_cmd = ['/bin/tar', '-xzf', tar_file, '-C', dest_dir]
    subprocess.run(tar_cmd, check=True)
