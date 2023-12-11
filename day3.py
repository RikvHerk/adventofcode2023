import numpy as np

inp = np.genfromtxt("day3.txt", dtype = str, comments = None)

inp = np.insert(inp, 0, "."*142)
inp = np.append(inp, "."*142)
for i, line in enumerate(inp):
    inp[i] = "." + line + "."

coordinates = []
s = 0

for y, line in enumerate(inp):
    found = False
    for x in range(len(line)):
        if line[x].isdigit():
            if not found:
                c = x
                found = True
        else:
            if found:
                coordinates.append([c, x, y])
                found = False

for c in coordinates:
    symbols = inp[c[2]-1][c[0]-1:c[1]+1] + inp[c[2]+1][c[0]-1:c[1]+1] + inp[c[2]][c[0]-1] + inp[c[2]][c[1]]
    for i in symbols:
        if i != ".":
            s += int(inp[c[2]][c[0]:c[1]])
    
print(s)