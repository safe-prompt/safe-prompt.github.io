import logging

def safe_read(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception:
        logging.error("An error occurred while reading the file.")
        return "Could not read file"
