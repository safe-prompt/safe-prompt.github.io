def save_user_data(filename, data):
    if '..' in filename or filename.startswith('/'):
        raise ValueError("Invalid filename.")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)