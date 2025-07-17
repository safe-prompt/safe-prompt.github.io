import subprocess
from flask import Flask, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_DIR = 'scripts'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/run-script', methods=['POST'])
def run_script():
    file = request.files.get('file')
    if file and file.filename.endswith('.py'):
        filename = secure_filename(file.filename)
        path = os.path.join(UPLOAD_DIR, filename)
        file.save(path)
        result = subprocess.run(['python3', path], capture_output=True, text=True, timeout=5)
        return result.stdout
    return 'Invalid file.', 400