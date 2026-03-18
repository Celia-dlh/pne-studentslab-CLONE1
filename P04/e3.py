import socket

IP = "127.0.0.1"
PORT = 8080

def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")
    lines = req.split('\n')
    req_line = lines[0]

    print("Request:", req_line)

    if "GET /info/A " in req_line:
        with open("html/info/A.html", "r") as i:
            body = i.read()

        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"

        response = status_line + header + "\n" + body
    elif "GET /info/C " in req_line:
        with open("html/info/C.html", "r") as i:
            body = i.read()

        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"

        response = status_line + header + "\n" + body

    else:
        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += "Content-Length: 0\n"

        response = status_line + header + "\n"

    s.send(response.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("server configured!")


while True:
    print("Waiting for clients....")
    try:
        (s, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped!")
        ls.close()
        exit()
    else:
        process_client(s)
        s.close()
