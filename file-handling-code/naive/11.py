def save_content_to_file(filename, content):
    if not filename.isalnum():
        raise ValueError("Invalid filename.")
    with open(f"{filename}.txt", 'w', encoding='utf-8') as f:
        f.write(content)