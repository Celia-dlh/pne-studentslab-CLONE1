# ex 1
a = 0
b = 1
print ( a , end=" ")
print ( b , end=" ")
for i in range (9):  # You have 2 first 9 + 2 = 11
    c = a + b
    print ( c , end= " ") # first 3
    a = b                 # change of variable
    b = c
