from Seq1 import Seq

s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
seq_list = [s1, s2, s3]

print("-----| Practice 1, Exercise 4 |------")
print(f"Sequence 1: (Length: {s1.len()}) {s1}")
print(f"Sequence 2: (Length: {s2.len()}) {s2}")
print(f"Sequence 3: (Length: {s3.len()}) {s3}")

