def compress_user_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError("File does not exist.")
    subprocess.run(['gzip', filepath], check=True)