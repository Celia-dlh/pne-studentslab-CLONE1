#ex 2

def fibon(n):
    a = 0
    b = 1
    for i in range(n - 1):
        c = a + b
        a = b  # change of variable
        b = c

    return c

n5 = fibon(5)
n10 = fibon(10)
n15 = fibon(15)
print(f"the 5th Fibonacci term: {n5} \nthe 10th Fibonacci term: {n10} \nthe 15th Fibonacci term: {n15}")

