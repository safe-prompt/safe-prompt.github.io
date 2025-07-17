import re
import os

def write_to_txt_file(filename, content):
    allowed_dir = "/home/user_data"
    if not re.match(r'^[\w\-]+\.txt$', filename):
        raise ValueError("Invalid filename format")
    filepath = os.path.join(allowed_dir, filename)
    with open(filepath, 'w') as f:
        f.write(content)
