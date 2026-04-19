import http.server
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        url = urlparse(self.path)
        path = url.path
        args = parse_qs(url.query)

        if path == "/":
            contents = Path("html/form-e1.html").read_text()

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents))
            self.end_headers()

            self.wfile.write(contents.encode())

        elif path == "/echo":
            msg = args.get("msg", [""])[0]

            contents = "<html><body>"
            contents += "<h1>" + msg + "</h1>"
            contents += '<a href="/">Return</a>'
            contents += "</body></html>"

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents))
            self.end_headers()

            self.wfile.write(contents.encode())

        else:
            contents = Path("html/error.html").read_text()

            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents))
            self.end_headers()

            self.wfile.write(contents.encode())


Handler = Handler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    httpd.serve_forever()