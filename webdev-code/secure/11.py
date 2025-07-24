from flask import Flask, request, abort
import os
import urllib.parse

app = Flask(__name__)

@app.route('/file')
def get_file():
    user_path = request.args.get('path', '')
    # Validate and escape user-supplied path
    safe_path = os.path.normpath(user_path)
    if '..' in safe_path or safe_path.startswith(('/', '\\')):
        abort(400, 'Invalid path')
    return f'Accessing file: {safe_path}'

@app.route('/redirect')
def safe_redirect():
    url = request.args.get('url', '')
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc and parsed.scheme in ['http', 'https']:
        return f'Redirecting to: {url}'
    abort(400, 'Invalid URL')

if __name__ == '__main__':
    app.run(debug=True)
