from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    resp = Response('Clickjacking protection enabled!')
    resp.headers['X-Frame-Options'] = 'DENY'
    return resp

if __name__ == '__main__':
    app.run(debug=True)
