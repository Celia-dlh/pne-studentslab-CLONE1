# option 1
    #f = open("dna.txt" , "r")
    #lines = f.readlines()
    # f.close()

from  dna_count_funtion import count_bases
if __name__ == " __main__":

    with open("dna.txt" , "r") as f: #the same but you don't have to close, is saver
        lines = f.readlines()

    total_number = 0
    bases = {"A": 0 , "C": 0 ,"T": 0 ,"G": 0}

    for seq in lines:
        seq = seq.strip() #remove space and realine seq
        total_number += len(seq)
        result = count_bases(seq)
        for key in result:
            bases[key] += result[key]


    print("Total number of bases:" , total_number)
    for base, count in bases.items():
        print(f"{base}: {count}")
