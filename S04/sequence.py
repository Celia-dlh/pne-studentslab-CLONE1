#  Write a program that opens the ADA.txt file and writes the total number of bases (have in mind that you should remove the new line ('\n') characters
#
# Considerations:
#
# Remove the first line (the header) and all the '\n' characters. Then the total number of bases can be calculated using the len() function
# The correct result is: 68557

from pathlib import Path
FILENAME = "sequences/ADA.txt"
file_contents = Path(FILENAME).read_text()
lines = file_contents.split("\n")

total = 0
for line in lines[1:]:
    total += len (line)
print (total)


