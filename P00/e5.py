from Seq0 import seq_count
from Seq0 import seq_read_fasta

print ("-----| Exercise 5 |------")
gens_list = ["U5" , "ADA" , "FRAT1" , "FXN"]

if __name__ == "__main__":
    for gene in gens_list:
        FOLDER = "../S04/sequences/"
        FILENAME = gene + ".txt"
        seq = seq_read_fasta(FOLDER + FILENAME)
        print(f"Gene {gene}: {seq_count(seq)}")