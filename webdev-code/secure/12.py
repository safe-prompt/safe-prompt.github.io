from flask import Flask, session, make_response

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.after_request
def set_hsts(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.set_cookie('session', session.sid, httponly=True, secure=True)
    return response

@app.route('/')
def index():
    session['user'] = 'secure_user'
    return 'HSTS and secure cookies set!'

if __name__ == '__main__':
    app.run(debug=True)
