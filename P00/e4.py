from Seq0 import seq_count_base
from Seq0 import seq_read_fasta

print ("-----| Exercise 4 |------")

gens_list = ["U5" , "ADA" , "FRAT1" , "FXN"]
bases = ["A" , "C" , "T" , "G"]
if __name__ == "__main__":
    for gene in gens_list:
        FOLDER = "../S04/sequences/"
        FILENAME = gene + ".txt"
        seq = seq_read_fasta(FOLDER + FILENAME)
        print(f"Gene {gene}:")
        for base in bases:
            print(f"  {base}: {seq_count_base(seq,base)}")
