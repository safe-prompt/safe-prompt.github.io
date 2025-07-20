from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_DIR = '/non_executable_uploads'
ALLOWED_EXT = {'txt'}
app.config['UPLOAD_DIR'] = UPLOAD_DIR

@app.route('/upload_txt', methods=['POST'])
def upload_txt_file():
    file = request.files.get('file')
    if not file or '.' not in file.filename:
        return jsonify({'error': 'No file or invalid filename'}), 400
    ext = file.filename.rsplit('.', 1)[1].lower()
    if ext not in ALLOWED_EXT:
        return jsonify({'error': 'File type not allowed'}), 400
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_DIR'], filename)
    file.save(filepath)
    return jsonify({'message': 'File uploaded successfully'}), 200
