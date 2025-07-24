from flask import Flask, request
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/token', methods=['POST'])
def handle_token():
    token = request.form.get('token', '')
    # Do not log sensitive tokens
    logging.info('Token received (not logged)')
    return 'Token processed securely.'

@app.errorhandler(Exception)
def handle_error(e):
    # Avoid verbose error output
    return 'An error occurred.', 500

if __name__ == '__main__':
    app.run(debug=True)
