from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(file_path, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted = encryptor.update(data) + encryptor.finalize()
    with open(file_path + '.enc', 'wb') as f:
        f.write(iv + encrypted)

# Example usage:
# key = os.urandom(32)
# encrypt_file('id_rsa', key)
