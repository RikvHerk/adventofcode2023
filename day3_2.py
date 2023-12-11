import numpy as np

inp = np.genfromtxt("day3.txt", dtype = str, comments = None)

inp = np.insert(inp, 0, "."*142)
inp = np.append(inp, "."*142)
for i, line in enumerate(inp):
    inp[i] = "." + line + "."

coordinates = []
gears = []

for y, line in enumerate(inp):
    found = False
    for x in range(len(line)):
        if line[x] == "*":
            gears.append([x,y])
        if line[x].isdigit():
            if not found:
                c = x
                found = True
        else:
            if found:
                coordinates.append([c, x, y])
                found = False

s = 0

for g in gears:
    adj = []
    for c in coordinates:
        if g[0] > c[0]-2 and g[0] < c[1]+1 and g[1] < c[2]+2 and g[1] > c[2]-2:
            adj.append(c)
    if len(adj) == 2:
        s += int(inp[adj[0][2]][adj[0][0]:adj[0][1]])*int(inp[adj[1][2]][adj[1][0]:adj[1][1]])

print(s)