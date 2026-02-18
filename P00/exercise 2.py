from Seq0 import seq_read_fasta

FOLDER = "../S04/sequences/"
FILENAME = "U5.txt"
bases = seq_read_fasta(FOLDER+FILENAME)

print("DNA file: U5.txt")
print("The first 20 bases are:")
for base in bases[:20]:
    print(base , end="")
