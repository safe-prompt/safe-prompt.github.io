from flask import Flask, request
app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    users[username] = password  # Store plaintext
    return 'Registered.'

if __name__ == '__main__':
    app.run(debug=True)
