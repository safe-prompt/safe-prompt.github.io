from flask import Flask, request, redirect
import ssl

app = Flask(__name__)

@app.before_request
def enforce_https():
    if not request.is_secure:
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

if __name__ == '__main__':
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain('cert.pem', 'key.pem')  # Use valid certificate files
    app.run(ssl_context=context)
