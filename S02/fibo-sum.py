#exercise 3

def fibosum(n):
    a = 0
    b = 1
    total = 0
    for i in range (n):
        total += a
        c = a + b
        a = b
        b = c
    return total

n5 = fibosum(5)
n10 = fibosum(10)



print (f"Sum of the first 5 fibonacci series: {n5} \nSum of the first 10 fibonacci series: {n10}")