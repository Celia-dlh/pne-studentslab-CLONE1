from Seq0 import seq_complement
from Seq0 import seq_read_fasta

FOLDER = "../S04/sequences/"
FILENAME = "U5.txt"
bases = seq_read_fasta(FOLDER+FILENAME)

print("------| Exercise 7 |------\n"
      "Gene U5")
print ("Frag: " , end="")
for base in bases[:20]:
    print(base, end="")

print ("\nComp: " , end="")
for base in bases[:20]:
    print (seq_complement(base), end="")

