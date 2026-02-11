# ex 2

text = "  Hello, World! Welcome to Python Programming.  "
new_text = text.strip('" "')

print ( f" Stripped: {new_text}")
print ( f" Word count: {len(text.split())}")
print ( f" Title case: {new_text.title()}")
print ( f" Starts with Hello: {new_text.startswith("Hello")}")
print ( f" Ends with ing: {new_text.endswith("ing.")}")
print ( f" Python position: {new_text.find("Python")}")
print ( f" Joined: {" - ".join(text.split())} ")


