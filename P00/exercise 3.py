from Seq0 import seq_read_fasta
from Seq0 import seq_len

gens_list = ["U5" , "ADA" , "FRAT1" , "FXN"]

print("-----| Exercise 3 |------")
if __name__ == "__main__":
    for gene in gens_list:
        FOLDER = "../S04/sequences/"
        FILENAME = gene + ".txt"
        seq = seq_read_fasta(FOLDER+FILENAME)
        print (f"Gene {gene} -> Length: {seq_len(seq)}")




