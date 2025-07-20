def print_file_contents(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")