#EX 3

lines = [ "AGTACACTGGT" ,"ACCAGTGTACT" , "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"]  #suppose they are always correct


def count_bases(seq):
    bases = {"A": 0 , "C": 0 ,"T": 0 ,"G": 0}
    for base in lines[seq]:
        if base in bases:
            bases[base] += 1
    return bases

seq1 = count_bases(0)
seq2 = count_bases(1)
seq3 = count_bases(2)

print ( f"Total number of bases 1º sequence: {len(lines[0])}\n{seq1}\n"
        f"Total number of bases 2º sequence: {len(lines[1])}\n{seq2}\n"
        f"Total number of bases 3º sequence: {len(lines[2])}\n{seq3}\n")

#totaly

total_number = 0
for seq in lines:
    total_number += len(seq)

bases = {"A": 0 , "C": 0 ,"T": 0 ,"G": 0}
for seq in lines:
    seq = seq.strip()
    total_number += len(seq)

    for base in seq:
        if base in seq:
         bases[base] += 1


for base, count in bases.items():
    print("Total number of bases", total_number)

# option 1
    #f = open("dna.txt" , "r")
    #lines = f.readlines()
    # f.close()

from  dna_count_funtion import count_bases
if __name__ == " __main__":

    with open("dna.txt" , "r") as f: #the same but you don't have to close, is saver
        lines = f.readlines()

    total_numbers = 0
    bases = {"A": 0 , "C": 0 ,"T": 0 ,"G": 0}

    for seq in lines:
        seq = seq.strip() #remove space and realine seq
        total_number += len(seq)
        result = count_bases(seq)
        for key in result:
            bases[key] += result[key]


    print("Total number of bases:" , total_number)
    for base, count in bases.items():
        print(f"{base}: {count}")
























