import socket
class Client:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT

    def __str__(self):
        return f"Connection to SERVER at {self.IP}, PORT: {self.PORT}"

    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.IP, self.PORT))

        s.send(str.encode(msg))

        response = s.recv(2048).decode("utf-8")

        s.close()
        return response

SERVER_IP = "127.0.0.1"
PORT = 8080

client = Client(SERVER_IP, PORT)
print("-----| Practice 3, Exercise 7 |------")
print(client)

print("* Testing PING...")
response = client.talk("PING")
print(response.strip())

print("\n* Testing GET...")
sequences = []
for i in range(5):
    response = client.talk(f"GET {i}")
    sequences.append(response.strip())
    print(f"GET {i}: {response.strip()}")

seq = sequences[0]

print("\n* Testing INFO...")
response = client.talk(f"INFO {seq}")
print(response.strip())

print("\n* Testing COMP...")
response = client.talk(f"COMP {seq}")
print(f"COMP {seq}")
print(response.strip())

print("\n* Testing REV...")
response = client.talk(f"REV {seq}")
print(f"REV {seq}")
print(response.strip())

print("\n* Testing GENE...")
genes_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in genes_list:
    response = client.talk(f"GENE {gene}")
    print(f"GENE {gene}")
    print(response.strip())