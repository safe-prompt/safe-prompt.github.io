from flask import Flask, request
app = Flask(__name__)

@app.route('/form', methods=['POST'])
def form():
    return 'CSRF protection disabled.'

if __name__ == '__main__':
    app.run(debug=True)
