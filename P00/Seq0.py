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

def seq_count_base(seq, base):
    return seq.count(base)

def seq_count(seq):
    bases = ["A" , "T" , "C" , "G"]
    bases_count = {}
    for base in bases:
        bases_count[base] = seq.count(base)
    return bases_count

def seq_reverse(seq):
    return seq[::-1]

def seq_complement(seq):
    complement_dict = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    complement = ""
    for base in seq:
        complement = complement_dict[base] + complement
    return complement