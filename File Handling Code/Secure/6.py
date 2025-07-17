import zipfile
import os

def safe_extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            abs_path = os.path.abspath(os.path.join(extract_to, member))
            if not abs_path.startswith(os.path.abspath(extract_to)):
                print(f"Skipping unsafe file: {member}")
                continue
            zip_ref.extract(member, extract_to)
