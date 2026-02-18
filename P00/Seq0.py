def seq_ping():
    print("OK")

def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    bases = file_contents.split("\n")
    base = "".join(bases[1:])
    return base

def seq_len(seq):
    return len(seq)


#def seq_count_base(seq, base):


#def seq_count(seq):


#def seq_reverse(seq):


#def seq_complement(seq):
