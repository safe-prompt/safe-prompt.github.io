from flask import Flask, request
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    password = request.form.get('password')
    # Use bcrypt for password hashing
    hashed = generate_password_hash(password, method='bcrypt')
    return f'Password hashed securely: {hashed}'

if __name__ == '__main__':
    app.run(debug=True)
