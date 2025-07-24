from flask import Flask, request, abort
import time

app = Flask(__name__)
login_attempts = {}
MAX_ATTEMPTS = 5
LOCKOUT_TIME = 60  # seconds

@app.route('/login', methods=['POST'])
def login():
    ip = request.remote_addr
    now = time.time()
    attempts = login_attempts.get(ip, {'count': 0, 'last': now})
    if attempts['count'] >= MAX_ATTEMPTS and now - attempts['last'] < LOCKOUT_TIME:
        abort(429, 'Too many attempts')
    # Log anomaly if needed
    # ...
    # Reset count if lockout expired
    if now - attempts['last'] > LOCKOUT_TIME:
        attempts = {'count': 0, 'last': now}
    attempts['count'] += 1
    attempts['last'] = now
    login_attempts[ip] = attempts
    return 'Login attempt logged.'

if __name__ == '__main__':
    app.run(debug=True)
