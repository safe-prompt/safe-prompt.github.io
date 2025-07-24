from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    user_input = request.args.get('input', '')
    return f'<h1>User input: {user_input}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
