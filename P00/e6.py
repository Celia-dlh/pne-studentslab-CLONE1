from Seq0 import seq_reverse
from Seq0 import seq_read_fasta

FOLDER = "../S04/sequences/"
FILENAME = "U5.txt"
bases = seq_read_fasta(FOLDER+FILENAME)

print("------| Exercise 6 |------\n"
      "Gene U5")

print ("Fragment: " , end="")
for base in bases[:20]:
    print(base, end="")

reverse = ""
for base in bases[:20]:
    reverse = seq_reverse(base) + reverse
print (f"\nReverse: {reverse}")