from flask import Flask, request, abort
import shlex
import subprocess

app = Flask(__name__)

@app.route('/run', methods=['POST'])
def run():
    cmd = request.form.get('cmd', '')
    # Sanitize input
    safe_cmd = shlex.split(cmd)
    if any(';' in part or '&&' in part for part in safe_cmd):
        abort(400, 'Invalid command')
    try:
        result = subprocess.run(safe_cmd, capture_output=True, text=True, timeout=5)
        return f'Output: {result.stdout}'
    except Exception:
        abort(400, 'Command failed')

if __name__ == '__main__':
    app.run(debug=True)
