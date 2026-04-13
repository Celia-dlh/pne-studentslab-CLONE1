import http.server
import socketserver
from pathlib import Path

PORT = 8080
bases = ["A", "C", "G", "T"]

socketserver.TCPServer.allow_reuse_address = True

class Handler (http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.strip("/")

        if path == "":
            filepath = Path("html/index.html")

        elif path.startswith("info/"):
            base = path.split("/")[-1]
            if base in bases:
                filepath = Path("html/info/" + base + ".html")
            else:
                filepath = Path("html/error.html")

        else:
            filepath = Path("html/" + path)

        try:
            content = filepath.read_bytes()
            self.send_response(200)
        except FileNotFoundError:
            content = Path("html/error.html").read_bytes()
            self.send_response(404)

        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(content))
        self.end_headers()
        self.wfile.write(content)

# Main server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by the user")
        httpd.server_close()
