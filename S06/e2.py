class Seq:

    def __init__(self, strbases):
        bases = ['A', 'C', 'G', 'T']

        for base in strbases:
            if base not in bases:
                print("INCORRECT Sequence detected")
                self.bases = "ERROR"
                return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

def print_seqs(seq_list):
    for i, seq in seq_list:
        print(f"Sequence {}: (Length: {len(seq.strbases)}) {seq}")

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)