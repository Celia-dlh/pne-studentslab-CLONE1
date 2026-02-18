# Write a program to analyze the ADA gene on human Chromosome 20, which is responsible for producing the adenosine deaminase enzyme. Your task is to download the exons information (file ADA_EXONS.txt) associated with the ADA-001 transcript and locate the exact starting index of each exon within this larger string. Because the gene is located on the reverse strand (-1), your script must implement a specific coordinate transformation where the first character of the file corresponds to the maximum chromosomal boundary of 44,652,852 (as specified in the FASTA header of the gene), meaning that as you move forward through the text sequence, the actual chromosomal coordinates decrease. The final output of your program should display each exon number, its length, and its precisely calculated start and end coordinates on Chromosome 20.

from pathlib import Path
FILENAME = "sequences/ADA_EXONS.txt"


