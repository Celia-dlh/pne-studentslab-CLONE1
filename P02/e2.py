from Client0 import Client

PRACTICE = 2
EXERCISE = 2
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.73" # my IP address
PORT = 8080
# -- Create a client object
c = Client(IP, PORT)
print (c)
