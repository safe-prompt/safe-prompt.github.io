from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://trusted.com"])  # Only allow trusted origins

@app.route('/')
def index():
    return 'CORS configured securely!'

if __name__ == '__main__':
    app.run(debug=True)
