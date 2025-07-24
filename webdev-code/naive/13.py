from flask import Flask
import os
app = Flask(__name__)

@app.route('/env')
def env():
    secrets = {k: os.environ[k] for k in ['SECRET_KEY', 'DB_PASSWORD'] if k in os.environ}
    return str(secrets)

if __name__ == '__main__':
    app.run(debug=True)
