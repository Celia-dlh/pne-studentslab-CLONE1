from Seq1 import Seq

FOLDER = "../S04/sequences/"
FILENAME = "U5.txt"
s = Seq()
s.read_fasta(FOLDER+FILENAME)

print("-----| Practice 1, Exercise 9 |------")
print(f"Sequence: (Length: {s.len()}) {s}")
print(f"  Bases: {s.count()}")
print(f"  Rev: {s.reverse()}")
print(f"  Comp: {s.complement()}")