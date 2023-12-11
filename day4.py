import numpy as np

inp = np.genfromtxt("day4.txt", dtype = str)
s = 0

for c in inp:
    points = -1
    for i in range(11):
        if c[i+2] in c[13:]:
            points += 1 
    if points > -1:
        s += 2**points

print(s)