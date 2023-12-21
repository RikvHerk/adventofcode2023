import numpy as np
import sys

sys.setrecursionlimit(10000)

def propagate(pos, direc):
    npos = pos + direc
    if pos[1]==-1:
        pos[1] = 0
    elif pos[1]==l:
        pos[1]=l-1
    elif pos[0]==-1:
        pos[0]=0
    elif pos[0]==l:
        pos[0]=l-1
    else:
        if list(direc) in energized[pos[0]][pos[1]] or any(npos>=l) or any(npos<0):
            energized[pos[0]][pos[1]].append(list(direc))
            return
        energized[pos[0]][pos[1]].append(list(direc))
    tile = grid[*npos]
    if tile == ".":
        propagate(npos, direc)
    if tile == "\\":
        if all(direc==right):
            propagate(npos, down)
        elif all(direc==left):
            propagate(npos, up)
        elif all(direc==up):
            propagate(npos, left)
        elif all(direc==down):
            propagate(npos, right)
    elif tile == "/":
        if all(direc==right):
            propagate(npos, up)
        elif all(direc==left):
            propagate(npos, down)
        elif all(direc==up):
            propagate(npos, right)
        elif all(direc==down):
            propagate(npos, left)
    elif tile == "|":
        if all(direc==right) or all(direc==left):
            propagate(npos, down)
            propagate(npos, up)
        elif all(direc==up) or all(direc==down):
            propagate(npos, direc)
    elif tile == "-":
        if all(direc==up) or all(direc==down):
            propagate(npos, right)
            propagate(npos, left)
        elif all(direc==right) or all(direc==left):
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

l=len(grid)

ss = []

for t in range(l):
    s = 0
    energized = [[[] for i in range(l)] for j in range(l)]
    propagate(np.array([t,-1]), right)
    for i in energized:
        for j in i:
            if j:
                s+=1
    ss.append(s)
    
for t in range(l):
    s = 0
    energized = [[[] for i in range(l)] for j in range(l)]
    propagate(np.array([t, l]), left)
    for i in energized:
        for j in i:
            if j:
                s+=1
    ss.append(s)

for t in range(l):
    s = 0
    energized = [[[] for i in range(l)] for j in range(l)]
    propagate(np.array([-1, t]), down)
    for i in energized:
        for j in i:
            if j:
                s+=1
    ss.append(s)
    
for t in range(l):
    s = 0
    energized = [[[] for i in range(l)] for j in range(l)]
    propagate(np.array([l, t]), up)
    for i in energized:
        for j in i:
            if j:
                s+=1
    ss.append(s)
            
print(max(ss))