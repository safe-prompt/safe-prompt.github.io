from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/set_cookie')
def set_cookie():
    session['data'] = 'value'
    # No HttpOnly or Secure flags
    return 'Cookie set.'

if __name__ == '__main__':
    app.run(debug=True)
