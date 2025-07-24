from flask import Flask, request
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(f'uploads/{file.filename}')
    return 'File uploaded.'

if __name__ == '__main__':
    app.run(debug=True)
