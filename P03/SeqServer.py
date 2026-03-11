from Seq1 import Seq
import socket
import termcolor

PORT = 8080
IP = "127.0.0.1"
bases = [ "A" , "T" , "C" , "G" ]
gens_list = ["U5" , "ADA" , "FRAT1" , "FXN" , "RNU6_269P"]
gens = {}
for gene in gens_list:
    FOLDER = "../S04/sequences/"
    FILENAME = gene + ".txt"

    seq = Seq()
    seq.read_fasta(FOLDER + FILENAME)
    gens[gene] = seq

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))

ls.listen()
print("Server SEQ configured!")

while True:
    print("Waiting for Clients...")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        txt = msg.split()
        command = txt[0]

        if command == "PING":
            print(termcolor.colored(f"{command} command!", 'green'))
            response = "OK! \n"
            print (response)

        elif command == "GET":
            arg = txt [1]
            n = int(arg)
            gene_name = gens_list[n]
            seq = gens[gene_name]

            response = seq.strbases + "\n"
            print(termcolor.colored( command, 'green'))
            print (response)

        elif command == "INFO":
            gene_name = gens_list[n]
            seq = gens[gene_name]

            gens[gene]

            print(f"Gene {gene}: Most frequent Base: {max(bases, key=bases.get)}")

        #elif command == "COMP":

        #elif command == "REV":

        #elif command == "GENE":


        cs.send(response.encode())
        cs.close()

