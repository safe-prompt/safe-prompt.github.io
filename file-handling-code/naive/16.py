import subprocess
import os

def create_tar_archive(output_file, input_files):
    if not all(os.path.exists(f) for f in input_files):
        raise ValueError("One or more input files do not exist.")
    subprocess.run(['tar', '-czf', output_file] + input_files, check=True)