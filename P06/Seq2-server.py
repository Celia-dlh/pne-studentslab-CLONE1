import http.server
import socketserver
from urllib.parse import parse_qs, urlparse
from pathlib import Path

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

sequences = ["AAAATTTGGCTCG","GGTGGGCGCGCTCCCACCTA","CCCACATTTGGTA","TAATATATATA","GCGGCGCGCAC"]

def read_gene(name):
    file_path = "../S04/sequences/" + name + ".txt"
    lines = Path(file_path).read_text().splitlines()
    sequence = "".join(lines[1:])
    return sequence

class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        url = urlparse(self.path)
        path = url.path
        args = parse_qs(url.query)

        if path == "/":
            contents = Path("html/index.html").read_text()

        elif path == "/ping":
            contents = "<html><body>"
            contents += "<h1>PING OK!</h1>"
            contents += "The SEQ2 server is running<br><br>"
            contents += "<a href='/'>Main page</a>"
            contents += "</body></html>"

        elif path == "/get":
            n = int(args.get("n", [0])[0])
            seq = sequences[n]

            contents = "<html><body>"
            contents += "<h1>SEQ SEQUENCE " + str(n) + "</h1>"
            contents += seq + "<br><br>"
            contents += "<a href='/'>Main page</a>"
            contents += "</body></html>"

        elif path == "/gene":
            name = args.get("name", [""])[0]
            seq = read_gene(name)

            contents = "<html><body>"
            contents += "<h1>GENE: " + name + "</h1>"
            contents += seq + "<br><br>"
            contents += "<a href='/'>Main page</a>"
            contents += "</body></html>"


        elif path == "/operation":
            seq = (args.get("seq", [""])[0]).upper()
            op = args.get("op", [""])[0]

            contents = "<html><body>"
            contents += "<h2>Sequence</h2>"
            contents += seq + "<br><br>"
            contents += "<h2>Operation</h2>"
            contents += op + "<br><br>"
            contents += "<h2>Result</h2>"

            if op == "rev":
                result = seq[::-1]
                contents += result

            elif op == "comp":
                comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
                result = ""
                for i in seq:
                    result += comp[i]
                contents += result

            elif op == "info":
                total = len(seq)
                a = seq.count("A")
                c = seq.count("C")
                g = seq.count("G")
                t = seq.count("T")

                contents += "Total length: " + str(total) + "<br>"
                contents += "A: " + str(a) + " (" + str(round(a / total * 100, 1)) + "%)<br>"
                contents += "C: " + str(c) + " (" + str(round(c / total * 100, 1)) + "%)<br>"
                contents += "G: " + str(g) + " (" + str(round(g / total * 100, 1)) + "%)<br>"
                contents += "T: " + str(t) + " (" + str(round(t / total * 100, 1)) + "%)<br>"

            contents += "<br><a href='/'>Main page</a>"
            contents += "</body></html>"

        else:
            contents = Path("html/error.html").read_text()

        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.send_header("Content-Length",len(contents))
        self.end_headers()
        self.wfile.write(contents.encode())

Handler = Handler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()