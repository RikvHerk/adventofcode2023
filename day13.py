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

s = 0
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
            s += column + 1
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
            s += 100*(row+1)
            break
print(s)