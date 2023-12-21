import numpy as np

def north():
    for i in range(ncol):
        for j in range(nrow):
            if grid[j, i] == "O":
                for k in np.arange(j-1, -2, -1):
                    if k == -1 or grid[k, i] in ["O", "#"]:
                        grid[j, i] = "."
                        grid[k + 1, i] = "O"
                        break
def south():
    for i in range(ncol):
        for j in np.arange(nrow-1, -1, -1):
            if grid[j, i] == "O":
                for k in np.arange(j+1, nrow+1):
                    if k == nrow or grid[k, i] in ["O", "#"]:
                        grid[j, i] = "."
                        grid[k - 1, i] = "O"
                        break

def west():
    for j in range(ncol):
        for i in range(nrow):
            if grid[j, i] == "O":
                for k in np.arange(i-1, -2, -1):
                    if k == -1 or grid[j, k] in ["O", "#"]:
                        grid[j, i] = "."
                        grid[j, k + 1] = "O"
                        break

def east():
    for j in range(ncol):
        for i in np.arange(ncol-1, -1, -1):
            if grid[j, i] == "O":
                for k in np.arange(i+1, ncol+1):
                    if k == ncol or grid[j, k] in ["O", "#"]:
                        grid[j, i] = "."
                        grid[j, k - 1] = "O"
                        break

def calc_load():
    s = 0
    for i in range(ncol):
        for j in range(nrow):
            if grid[j, i] == "O":
                s += nrow - j
    return s
                
with open("day14.txt", 'r') as inp:
    lines = inp.readlines()
    
grid = []
for line in lines:
    grid.append([i for i in line[:-1]])
grid[-1] = [i for i in lines[-1]]

grid = np.array(grid)

nrow = len(grid[:, 0])
ncol = len(grid[0, :])

x = []
for i in range(1000):
    north()
    west()
    south()
    east()
    x.append(calc_load())
x = np.array(x)
period = np.where(x==x[-1])[0]
print(x[-1])