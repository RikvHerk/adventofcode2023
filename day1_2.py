import numpy as np

inp = np.genfromtxt("day1.txt", dtype = str)

s = 0
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for n in inp:
    digits = []
    for i in range(len(n)):
        if n[i].isdigit():
            digits.append(n[i])
            continue
        for j, k in enumerate(numbers):
            if k == n[i:i+len(k)]:
                digits.append(str(j+1))
    
    s += int(digits[0] + digits[-1])

print(s)


