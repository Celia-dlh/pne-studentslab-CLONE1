import http.server
import socketserver
from pathlib import Path

PORT = 8080
bases = ["A", "C", "G", "T"]
HTML_DIR = Path("html")


class BasesHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"GET received! Requested path: {self.path}")
        filepath = None

        if self.path == "/" or self.path == "/index.html":
            filepath = HTML_DIR / "index.html"

        elif self.path.startswith("/info/"):
            base = self.path.split("/")[-1]
            if base in bases:
                filepath = HTML_DIR / "info" / f"{base}.html"
            else:
                filepath = HTML_DIR / "error.html"

        else:
            filename = self.path.strip("/")
            filepath = HTML_DIR / filename

        try:
            content = filepath.read_bytes()
        except FileNotFoundError:
            error_path = HTML_DIR / "error.html"
            content = error_path.read_bytes()

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(content))
        self.end_headers()
        self.wfile.write(content)

# Main server

Handler = BasesHandler
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by the user")
        httpd.server_close()
