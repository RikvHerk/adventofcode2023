import numpy as np

def hash(i):
    s = 0
    for j in i:
        s += ord(j)
        s *= 17
        s %= 256
    return s

inp = np.genfromtxt("day15.txt", dtype=str, delimiter=",")

s = 0
for i in inp:
    s += hash(i)

print(s)