from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.73" # my IP
PORT = 8080
#  Create a client object
c = Client(IP, PORT)
print (c)
#  Send a message to the server
genes = ["U5", "FRAT1", "ADA"]
for gene in genes:
    s = Seq()
    info_message = f"Sending the {gene} Gene to the server..."
    print (info_message)
    FOLDER = "../S04/sequences/"
    FILENAME = gene + ".txt"
    s.read_fasta(FOLDER + FILENAME)
    c.talk(info_message)

    gene_sequence = str(s)
    print(gene_sequence)
    c.talk(gene_sequence)
