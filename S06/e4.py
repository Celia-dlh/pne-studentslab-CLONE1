import termcolor
class Seq:
    def __init__(self, strbases):
        bases = ["A", "C", "G", "T"]
        for base in strbases:
            if base not in bases:
                print("INCORRECT Sequence detected")
                self.strbases = "ERROR"
                return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def __len__(self):
        return len(self.strbases)

def generate_seqs(pattern, number):
    seqs = []
    for i in range (number):
        seqs.append(Seq((i + 1) * pattern))
    return seqs

def print_seqs(seq_list , color):
    i = 0
    for seq in seq_list:
        termcolor.cprint(f"Sequence {i}: (Length: {len(seq.strbases)}) {seq}" , color)
        i += 1

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:" , "blue")
print_seqs(seq_list1 , "blue")

print()
termcolor.cprint("List 2:" , "green")
print_seqs(seq_list2 , "green")