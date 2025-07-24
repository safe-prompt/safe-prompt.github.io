from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join('uploads', file.filename))
    os.chmod(os.path.join('uploads', file.filename), 0o777)
    return 'File uploaded.'

if __name__ == '__main__':
    app.run(debug=True)
