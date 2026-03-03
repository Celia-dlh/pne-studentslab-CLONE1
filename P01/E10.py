from Seq1 import Seq
gens_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
print("-----| Practice 1, Exercise 10 |------")
for gene in gens_list:
    FOLDER = "../S04/sequences/"
    FILENAME = gene + ".txt"

    seq = Seq()
    seq.read_fasta(FOLDER + FILENAME)
    bases = seq.count()

    print(f"Gene {gene}: Most frequent Base: {max(bases, key=bases.get)}")
