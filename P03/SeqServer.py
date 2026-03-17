from Seq1 import Seq
import socket
import termcolor

PORT = 8080
IP = "127.0.0.1"
bases = [ "A" , "T" , "C" , "G" ]
genes_list = ["U5" , "ADA" , "FRAT1" , "FXN" , "RNU6_269P"]
FOLDER = "../S04/sequences/"

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

            gene_name = genes_list[n]
            seq = Seq()
            seq.read_fasta(FOLDER + gene_name + ".txt")
            response = seq.strbases + "\n"
            print(termcolor.colored( command , 'green'))
            print(response)

        elif command == "INFO":
            arg = txt[1]
            seq = Seq(arg)
            length = seq.len()
            counts = seq.count()

            response = f"Sequence: {seq} \nTotal length: {length}\n"

            for i in bases:
                count = counts[i]
                perc = round((count / length * 100) , 1)
                response += f"{i}: {count} ({perc}%) \n"

            print(termcolor.colored(command, 'green'))
            print(response)

        elif command == "COMP":
            arg = txt[1]
            seq = Seq(arg)
            comp = seq.complement()
            response = comp + "\n"
            print(termcolor.colored( command, 'green'))
            print(arg)
            print(response)

        elif command == "REV":
            arg = txt[1]
            seq = Seq(arg)
            rev = seq.reverse()
            response = rev + "\n"
            print(termcolor.colored(command, 'green'))
            print(arg)
            print(response)

        elif command == "GENE":
            gene_name = txt[1]
            if gene_name not in genes_list:
                response = "ERROR: Invalid gene name\n"
            else:
                seq = Seq()
                seq.read_fasta(FOLDER + gene_name + ".txt")
                response = seq.strbases + "\n"
                print(termcolor.colored(command, 'green'))
                print(response)


        cs.send(response.encode())
        cs.close()

