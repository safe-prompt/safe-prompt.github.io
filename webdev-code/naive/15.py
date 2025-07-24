from flask import Flask, request, send_from_directory
app = Flask(__name__)

@app.route('/file')
def file():
    path = request.args.get('path', '')
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
