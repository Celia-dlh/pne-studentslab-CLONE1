# Write a program that opens the U5.txt file and prints all the lines except the first one (the header)

from pathlib import Path
FILENAME = "sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
lines = file_contents.split("\n")

for line in lines[1:]:
    print(line)
