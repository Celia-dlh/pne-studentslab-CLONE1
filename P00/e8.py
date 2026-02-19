from Seq0 import seq_read_fasta
from Seq0 import seq_count

gens_list = ["U5" , "ADA" , "FRAT1" , "FXN"]

for gene in gens_list:
    FOLDER = "../S04/sequences/"
    FILENAME = gene + ".txt"
    seq = seq_read_fasta(FOLDER + FILENAME)
    bases = seq_count(seq)
    print(f"{gene}: Most frequent Base: {max(bases , key = bases.get )}")
    
    
