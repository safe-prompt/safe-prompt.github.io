import jwt
from flask import Flask, request, abort
from jwt import InvalidSignatureError

app = Flask(__name__)
SECRET = 'supersecretkey'

@app.route('/verify', methods=['POST'])
def verify():
    token = request.form.get('token', '')
    try:
        payload = jwt.decode(token, SECRET, algorithms=['HS256'])
        return f'JWT verified: {payload}'
    except InvalidSignatureError:
        abort(401, 'Invalid signature')
    except Exception:
        abort(400, 'Invalid token')

if __name__ == '__main__':
    app.run(debug=True)
