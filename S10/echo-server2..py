import socket
import termcolor

# This is going to be version 1. We will create the socket, bind it to its IP and PORT parameters and configure it for being a listening socket.
# Finaly we will close the socket.

PORT = 8080
IP = "212.128.255.82"
number_con = 0
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
print("The server is configured!")

while True:
    print("Waiting for Clients to connect")

    number_con += 1
    print("CONNECTION: {}. Client IP, PORT: ({}, {})".format(number_con, IP , PORT))

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        termcolor.cprint(f"ECHO: {msg}", 'green')

        response = f"ECHO:  {msg}\n"
        cs.send(response.encode())
        cs.close()

