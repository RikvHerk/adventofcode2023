import numpy as np
import matplotlib.pyplot as plt

def cost(path, pos):
    s = -grid[*pos]
    for p in path:
        s += grid[*pos]
        pos += p
    return s

with open("day17.txt", 'r') as inp:
    lines = inp.readlines()
    
grid = []
for line in lines:
    grid.append([int(i) for i in line[:-1]])
grid[-1] = [int(i) for i in lines[-1]]

grid = np.array(grid)

right = np.array([0, 1])
left = np.array([0, -1])
up = np.array([-1, 0])
down = np.array([1, 0])

path = []
for i in range(2*(len(grid))-1):
    if i%2==0:
        path.append(right)
    else:
        path.append(down)

s = 0
seg = []
for p in path:
    s += sum(p)
    seg.append(p)
    if s == 6:
        break

print(cost(path, np.array([0,0])))
    
