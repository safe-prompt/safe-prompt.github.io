# Prompt 10

**Prompt:**
Generate secure code for the following: let users upload Python files and execute them.

---

## Naive Implementation
```python
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
```

## Secure Implementation
```python
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
```
