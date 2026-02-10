#ex 2
seq = str (input ("Introduce the sequence:"))  #suppose is always right

A = 0
C = 0
T = 0
G = 0
for i in seq:
    if i == "A":
        A += 1
    if i == "C":
        C += 1
    if i == "T":
        T += 1
    if i == "G":
        G += 1

print(f"Total length: {len(seq)}")
print(f"A: {A} \nC: {C} \nT: {T} \ng: {G}")

#other way ( prof)
bases = {"A": 0 , "C": 0 ,"T": 0 ,"G": 0 }

for base in seq:
    if base in bases:
        bases[base] += 1

print (bases)
