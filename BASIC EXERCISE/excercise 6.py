#ex 6.a

def is_even(number):
    return number % 2 == 0

print( f" is_even(4) = {is_even(4)}")
print( f" is_even(7) = {is_even(7)}")
print( f" is_even(0) = {is_even(0)}")
print( f" is_even(-3) = {is_even(-3)}")
print( f" is_even(10) = {is_even(10)}")

#ex 6.b

def classify_triangle(a, b, c):
    if a == b == c :
        return "equilateral"
    elif a == b or b == c or a == c:
        return "isosceles"
    elif a != b != c :
        return "scalene"
print (f"\nTriangles sides:")
print (f"classify_triangle(5, 5, 5) = {classify_triangle(5, 5, 5)}")
print (f"classify_triangle(3, 3, 4) = {classify_triangle(3, 3, 4)}")
print (f"classify_triangle(3, 4, 5) = {classify_triangle(3, 4, 5)}")