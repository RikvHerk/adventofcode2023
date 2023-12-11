import numpy as np

inp = np.genfromtxt("day1.txt", dtype = str)

s = 0

for n in inp:
    digits = []
    for i in range(len(n)):
        if n[i].isdigit():
            digits.append(n[i])
    
    s += int(digits[0] + digits[-1])

print(s)


