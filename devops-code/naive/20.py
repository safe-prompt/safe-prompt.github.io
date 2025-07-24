from http.server import HTTPServer, SimpleHTTPRequestHandler

def run_server():
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    print("Serving on 0.0.0.0:8000")
    server.serve_forever()

run_server()
