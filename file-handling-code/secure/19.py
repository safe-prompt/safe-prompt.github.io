from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
NON_EXEC_UPLOADS = '/safe_storage'
ALLOWED_EXTS = {'txt', 'pdf'}

@app.route('/safe_upload', methods=['POST'])
def safe_upload():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    ext = file.filename.rsplit('.', 1)[-1].lower()
    if ext not in ALLOWED_EXTS:
        return jsonify({'error': 'Disallowed file type'}), 400
    filename = secure_filename(file.filename)
    path = os.path.join(NON_EXEC_UPLOADS, filename)
    file.save(path)
    os.chmod(path, 0o600)
    return jsonify({'message': 'Upload successful'}), 200
