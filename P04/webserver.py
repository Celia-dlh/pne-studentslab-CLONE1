import socket

IP = "127.0.0.1"
PORT = 8080

bases = [ "A" , "C" , "G" , "T"]

def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")
    lines = req.split('\n')
    req_line = lines[0]

    print("Request:", req_line)

    flag = False
    if "GET / " in req_line:
        with open("html/index.html", "r") as i:
            body = i.read()

        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"

        response = status_line + header + "\n" + body
        s.send(response.encode())
        flag = True

    for base in bases:
        if f"GET /info/{base} " in req_line:
            with open(f"html/info/{base}.html", "r") as i:
                body = i.read()

            status_line = "HTTP/1.1 200 OK\n"
            header = "Content-Type: text/html\n"
            header += f"Content-Length: {len(body)}\n"
            response = status_line + header + "\n" + body
            s.send(response.encode())
            flag = True

    if not flag:
        with open(f"html/error.html", "r") as i:
            body = i.read()

        status_line = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n"
        header += f"Content-Length: {len(body)}\n"
        response = status_line + header + "\n" + body
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