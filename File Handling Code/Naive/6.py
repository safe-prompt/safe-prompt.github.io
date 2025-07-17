import zipfile
import os

def extract_zip(archive_path, extract_to):
    if not zipfile.is_zipfile(archive_path):
        raise ValueError("Invalid zip file.")
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(path=extract_to)