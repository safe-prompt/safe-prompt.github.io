from flask import Flask, session, make_response

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    session['user'] = 'secure_user'
    resp = make_response('Session set securely!')
    resp.set_cookie('session', session.sid, httponly=True, secure=True)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
