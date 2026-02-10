def count_bases(seq):
    bases = {"A": 0, "C": 0, "T": 0, "G": 0}

    for base in seq:
        if base in bases:
            bases[base] += 1
    return bases


if __name__= " __name__":
    SEQUENCE =  input("Introduce sequence:" )
    print("Total length:" , len(seq))

    result =