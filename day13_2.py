import numpy as np

with open("day13.txt", 'r') as inp:
    lines = inp.readlines()

grids = []
grid = []
for line in lines:
    if line == "\n":
        grids.append(np.array(grid))
        grid = []
    else:
        grid.append([i for i in line[:-1]])
grid[-1] = [i for i in lines[-1]]
grids.append(np.array(grid))

old = []

for grid in grids:
    for column in range(len(grid[0])-1):
        f = True
        for c in np.arange(column+1):
            if 2*column-c+1 > len(grid[0])-1:
                continue
            if not all(grid[:,c] == grid[:, 2*column-c+1]):
                f = False
                break
        if f:
            old.append([column, -1])
            break
        
    if f:
        continue
    
    for row in range(len(grid)-1):
        f = True
        for r in range(row+1):
            if 2*row-r+1 > len(grid)-1:
                continue
            if not all(grid[r] == grid[2*row-r+1]):
                f = False
                break
        if f:
            old.append([-1, row])
            break
s = 0

for i, grid in enumerate(grids):
    for column in range(len(grid[0])-1):
        if column == old[i][0]:
            continue
        f = True
        smudge = 0
        for c in np.arange(column+1):
            if 2*column-c+1 > len(grid[0])-1:
                continue
            mirror = grid[:,c] == grid[:, 2*column-c+1]
            smudge += len(mirror)-sum(mirror)
            if smudge > 1:
                f = False
                break
        if f:
            s += column + 1
            break
        
    if f:
        continue
    
    for row in range(len(grid)-1):
        if row == old[i][1]:
            continue
        f = True
        smudge = 0
        for r in range(row+1):
            if 2*row-r+1 > len(grid)-1:
                continue
            mirror = grid[r] == grid[2*row-r+1]
            smudge += len(mirror)-sum(mirror)
            if smudge > 1:
                f = False
                break
        if f:
            s += 100*(row+1)
            break
print(s)