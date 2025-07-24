from flask import Flask, request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/store', methods=['POST'])
def store():
    data = request.form.get('data', '')
    encrypted = cipher_suite.encrypt(data.encode())
    # Store encrypted data securely (e.g., in a database)
    return f'Encrypted data: {encrypted}'

if __name__ == '__main__':
    app.run(debug=True)
