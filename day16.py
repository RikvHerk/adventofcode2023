import numpy as np
import sys

sys.setrecursionlimit(10000)

def propagate(pos, direc):
    npos = pos + direc
    if pos[1]==-1:
        pos[1] = 0
    if list(direc) in energized[pos[0]][pos[1]] or any(npos>=len(grid)) or any(npos<0):
        energized[pos[0]][pos[1]].append(list(direc))
        return
    energized[pos[0]][pos[1]].append(list(direc))
    tile = grid[*npos]
    if tile == ".":
        propagate(npos, direc)
    if tile == "\\":
        if all(direc==right):
            propagate(npos, down)
        if all(direc==left):
            propagate(npos, up)
        if all(direc==up):
            propagate(npos, left)
        if all(direc==down):
            propagate(npos, right)
    if tile == "/":
        if all(direc==right):
            propagate(npos, up)
        if all(direc==left):
            propagate(npos, down)
        if all(direc==up):
            propagate(npos, right)
        if all(direc==down):
            propagate(npos, left)
    if tile == "|":
        if all(direc==right) or all(direc==left):
            propagate(npos, down)
            propagate(npos, up)
        if all(direc==up) or all(direc==down):
            propagate(npos, direc)
    if tile == "-":
        if all(direc==up) or all(direc==down):
            propagate(npos, right)
            propagate(npos, left)
        if all(direc==right) or all(direc==left):
            propagate(npos, direc)

with open("day16.txt", 'r') as inp:
    lines = inp.readlines()

right = np.array([0, 1])
left = np.array([0, -1])
up = np.array([-1, 0])
down = np.array([1, 0])

grid = []
for line in lines:
    grid.append([i for i in line[:-1]])
grid[-1] = [i for i in lines[-1]]

grid = np.array(grid)
energized = [[[] for i in range(len(grid))] for j in range(len(grid))]

propagate(np.array([0,-1]), right)

s = 0

for i in energized:
    for j in i:
        if j:
            s+=1
            
print(s)