from cryptography.fernet import Fernet

def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_data(token, key):
    f = Fernet(key)
    return f.decrypt(token).decode()

# Example usage:
# key = Fernet.generate_key()
# encrypted = encrypt_data('secret', key)
# print(decrypt_data(encrypted, key))
