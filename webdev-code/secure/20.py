from flask import Flask

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_error(e):
    # Do not expose stack traces
    return 'An error occurred.', 500

@app.route('/')
def index():
    return 'Error handling is secure.'

if __name__ == '__main__':
    app.run(debug=True)
