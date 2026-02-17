# Description: Write a python program that opens the file RNU6_269P.txt and prints (only) its header:
# First line of the RNU6_269P.txt file:
# >16 dna:chromosome chromosome:GRCh38:16:58377452:58378748:-1

from pathlib import Path
FILENAME = "sequences/RNU6_269P.txt"
file_contents = Path(FILENAME).read_text()
print(file_contents.split("\n")[0])