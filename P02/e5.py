from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.73" # my IP
PORT = 8080

c = Client(IP, PORT)
print (c)

gene = "FRAT1"
s = Seq()
FOLDER = "../S04/sequences/"
FILENAME = gene + ".txt"

info_message = f"Sending {gene} Gene to the server, in fragments of 10 bases..."
print (info_message)
c.talk(info_message)

s.read_fasta(FOLDER + FILENAME)
gene_sequence = str(s)
print (f"Gene {gene}: {gene_sequence} ")

n = 0
for i in range(1, 6) :
    frag = gene_sequence[n : n + 10]
    fragments = f"Fragment {i}: {frag}"
    print (fragments)
    c.talk(fragments)
    n += 10
