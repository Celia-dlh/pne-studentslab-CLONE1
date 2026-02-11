#Ex 3  Lists

temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

def n_more ():
    n = 0
    for i in temperatures:
       if i > 17 :
           n += 1
    return n

print (f" Wednesday: {temperatures[2]} ")
print (f" Max: {max(temperatures)}")
print (f" Min: {min(temperatures)}")
print (f" Average: {round(sum(temperatures)/len(temperatures), 1)}")
print (f" Days above: {n_more ()}")
print (f" Sorted: {sorted(temperatures,reverse=True)}")
