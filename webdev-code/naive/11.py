from flask import Flask, request
import sqlite3
app = Flask(__name__)

@app.route('/user')
def user():
    name = request.args.get('name', '')
    conn = sqlite3.connect('users.db')
    query = f"SELECT * FROM users WHERE name = '{name}'"
    result = conn.execute(query).fetchall()
    conn.close()
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
