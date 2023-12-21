import numpy as np

with open("day14.txt", 'r') as inp:
    lines = inp.readlines()
    
grid = []
for line in lines:
    grid.append([i for i in line[:-1]])
grid[-1] = [i for i in lines[-1]]

grid = np.array(grid)

nrow = len(grid[:, 0])
ncol = len(grid[0, :])

s = 0
for i in range(ncol):
    for j in range(nrow):
        if grid[j, i] == "O":
            x = 0
            for k in np.arange(j-1, -2, -1):
                if k == -1:
                    s += nrow - x
                    break
                if grid[k, i] == "O":
                    x += 1
                elif grid[k, i] == "#":
                    s += nrow - k - x - 1
                    break

print(s)