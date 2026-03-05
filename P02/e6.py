from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.73" # my IP address
PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
print (c1)
print (c2)

gene = "FRAT1"
s = Seq()
FOLDER = "../S04/sequences/"
FILENAME = gene + ".txt"

info_message = f"Sending {gene} Gene to the server, in fragments of 10 bases..."
print (info_message)
c1.talk(info_message)
c2.talk(info_message)

s.read_fasta(FOLDER + FILENAME)
gene_sequence = str(s)
print (f"Gene {gene}: {gene_sequence} ")

n = 0
for i in range(1, 10 + 1) :
    frag = gene_sequence[n : n + 10]
    fragments = f"Fragment {i}: {frag}"
    print (fragments)
    if i % 2 == 0:
        c2.talk(fragments)
    else:
        c1.talk(fragments)
    n += 10
