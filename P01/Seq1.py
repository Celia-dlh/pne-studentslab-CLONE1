class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            print("NULL sequence created")
            self.strbases = "NULL"
            return

        bases = ["A", "C", "G", "T"]
        for base in strbases:
            if base not in bases:
                print("INVALID sequence!")
                self.strbases = "ERROR"
                return

        print("New sequence created!")
        self.strbases = strbases

    def __str__(self):
        if self.strbases == "NULL":
            return "NULL"
        if self.strbases == "ERROR":
            return "ERROR"
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return self.strbases.count(base)

    def count(self):
        base_count = {"A": 0, "T": 0, "C": 0, "G": 0}
        for base in self.strbases:
            if base in base_count:
                base_count[base] += 1
        return base_count

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        return self.strbases[::-1]

    def complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
        complement = ""
        for base in self.strbases:
            complement += complement_dict[base]
        return complement

    def read_fasta(self , filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        lines = file_contents.splitlines()
        strbases = "".join(lines[1:]).strip()
        self.strbases = strbases
