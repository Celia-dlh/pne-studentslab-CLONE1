from Client0 import Client

PRACTICE = 2
EXERCISE = 3
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.73" # my IP address
PORT = 8080
# -- Create a client object
c = Client(IP, PORT)
print (c)
# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
