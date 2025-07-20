import tempfile

def write_temp_file(data):
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, encoding='utf-8') as tmp:
        tmp.write(data)
        return tmp.name