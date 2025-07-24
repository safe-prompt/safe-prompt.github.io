from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    csp = "default-src 'self'; script-src 'self'; object-src 'none';"
    resp = Response('Content Security Policy set!')
    resp.headers['Content-Security-Policy'] = csp
    return resp

if __name__ == '__main__':
    app.run(debug=True)
