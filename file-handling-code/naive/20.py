def read_user_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError("File not found.")
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()