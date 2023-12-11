import numpy as np

with open("day11.txt", 'r') as inp:
    lines = inp.readlines()

for i in range(len(lines)-1):
    lines[i] = [j for j in lines[i][:-1]]
lines[i+1] = [j for j in lines[i+1]]

gmap = np.array(lines)


rows = []
columns = []
for i, row in enumerate(gmap):
    if not "#" in row:
        rows.append(i)
        
for i, column in enumerate(gmap.transpose()):
    if not "#" in column:
        columns.append(i)

g = []
for i in range(len(gmap)):
    for j in range(len(gmap)):
        if gmap[i,j] == "#":
            g.append([i,j])

s = 0
for i in range(len(g)):
    for j in range(len(g)-1-i):
        r = 0
        for row in rows:
            if row > g[i][0] and row < g[j+1+i][0] or row > g[j+1+i][0] and row < g[i][0]:
                r += 999999
        c = 0
        for column in columns:
            if column > g[i][1] and column < g[j+1+i][1] or column > g[j+1+i][1] and column < g[i][1]:
                c += 999999
        s += r + c + abs(g[i][0] - g[j+1+i][0]) + abs(g[i][1] - g[j+1+i][1])

print(s)