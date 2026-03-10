import socket
import termcolor

# This is going to be version 1. We will create the socket, bind it to its IP and PORT parameters and configure it for being a listening socket.
# Finally we will close the socket.

PORT = 8080
IP = "212.128.255.82" # MY IP
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
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    number_con += 1
    print("CONNECTION: {}. Client IP, PORT: ({}, {})".format(number_con, IP , PORT))
    c_tuples = (IP , PORT)

    try:
        (cs, client_ip_port) = ls.accept()

        # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

        # -- Execute this part if there are no errors
    else:

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-readable string
        msg = msg_raw.decode()

        # -- Print the received message
        termcolor.cprint(f"ECHO: {msg}", 'green')

        # -- Send a response message to the client
        response = f"ECHO:  {msg}\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())
        if number_con == 5 :
            for i in

        # -- Close the data socket
        cs.close()

print(f"Client {number_con}: {c_tuples}")
