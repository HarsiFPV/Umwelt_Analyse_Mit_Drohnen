from http.server import HTTPServer, BaseHTTPRequestHandler

host = "192.168.1.15"
port = 9999

class NeuralHTTP(BaseHTTPRequestHandler):
    def __init__(self):
        pass

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes"<html><body><h1>HELLO WORLD !!</h1></body></html>", "utf-8")

server = HTTPServer((host, port), NeuralHTTP)
print("Server now running on ", host, "port",port, "...")
server.serve_forever()
server.server_close()
print("Server stopped)")