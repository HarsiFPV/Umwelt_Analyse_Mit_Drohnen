from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import shutil
import socket

port = 9999

class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        index = self.get_folder_index()
        self.wfile.write(bytes(index, "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        success = self.copy_folder_contents()
        if success:
            self.wfile.write(bytes("Folder copied successfully.", "utf-8"))
        else:
            self.wfile.write(bytes("Failed to copy folder.", "utf-8"))

    def get_folder_index(self):
        files = os.listdir(".")
        index = "<html><body><ul>"

        for file_name in files:
            if os.path.isfile(file_name):
                index += "<li>" + file_name + "</li>"

        index += "</ul></body></html>"
        return index

    def copy_folder_contents(self):
        try:
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")

            # Get source and destination folder paths from POST data
            source_path, destination_path = post_data.strip().split(";")

            files = os.listdir(source_path)
            for file_name in files:
                if os.path.isfile(os.path.join(source_path, file_name)):
                    shutil.copy2(os.path.join(source_path, file_name), destination_path)

            return True
        except Exception as e:
            print("Error:", e)
            return False

def get_local_ip():
    # Create a socket to get the local IP address
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    ip_address = sock.getsockname()[0]
    sock.close()
    return ip_address

def main():
    host = get_local_ip()

    server = HTTPServer((host, port), NeuralHTTP)
    print("Server now running on", host, "port", port, "...")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
    print("Server stopped)")

if __name__ == "__main__":
    main()
