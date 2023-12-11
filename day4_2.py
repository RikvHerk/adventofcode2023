import numpy as np

inp = np.genfromtxt("day4.txt", dtype = str)
count = np.ones(len(inp)+10)

for j, c in enumerate(inp):
    points = 0
    for i in range(11):
        if c[i+2] in c[13:]:
            points += 1 
    count[j+1:j+1+points] += count[j]

print(np.sum(count[:len(inp)]))