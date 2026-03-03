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

def print_seqs(seq_list):
    i = 0
    for seq in seq_list:
        print(f"Sequence {i}: (Length: {len(seq.strbases)}) {seq}")
        i += 1

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
