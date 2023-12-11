import numpy as np

import sys

sys.setrecursionlimit(100000)

def mark(pos, direction):
    i = pos[0]
    j = pos[1]
    y = i
    x = j
    npos = (i + direction[0], j + direction[1])
    
    ndirection = maze[npos]
    path[pos] = 1
    
    if ndirection == "S" or 0:
        for m in range(l):
            if all([n!=1 for n in path[m]]):
                for k in range(l):
                    path[m,k] = 2
                    
    if direction == (0, -1):
        while y<l-1 and path[y+1, j] != 1:
            path[y+1, j] = 2
            y += 1
        if maze[pos] == "7":
            while x>-1 and path[i, x-1] != 1:
                path[i, x-1] = 2
                x -= 1
        if maze[pos] == "J":
            while x<l-1 and path[i, x+1] != 1:
                path[i, x+1] = 2
                x += 1 
        if ndirection == "L":
            return mark(npos, (-1, 0))
        if ndirection == "F":
            return mark(npos, (1, 0))
        if ndirection == "-":
            return mark(npos, (0, -1))
    if direction == (0, 1):
        while y>-1 and path[y-1, j] != 1:
            path[y-1, j] = 2
            y -= 1
        if maze[pos] == "F":
            while x>-1 and path[i, x-1] != 1:
                path[i, x-1] = 2
                x -= 1
        if maze[pos] == "L":
            while x<l-1 and path[i, x+1] != 1:
                path[i, x+1] = 2
                x += 1 
        if ndirection == "7":
            return mark(npos, (1, 0))
        if ndirection == "J":
            return mark(npos, (-1, 0))
        if ndirection == "-":
            return mark(npos, (0, 1))
    if direction == (-1, 0):
        while x>-1 and path[i, x-1] != 1:
            path[i, x-1] = 2
            x -= 1
        if maze[pos] == "J":
            while y>-1 and path[y-1, j] != 1:
                path[y-1, j] = 2
                y -= 1
        if maze[pos] == "L":
            while y<l-1 and path[y+1, j] != 1:
                path[y+1, j] = 2
                y += 1 
        if ndirection == "7":
            return mark(npos, (0, -1))
        if ndirection == "F":
            return mark(npos, (0, 1))
        if ndirection == "|":
            return mark(npos, (-1, 0))
    if direction == (1, 0):
        while x<l-1 and path[i, x+1] != 1:
            path[i, x+1] = 2
            x += 1
        if maze[pos] == "F":
            while y<l-1 and path[y+1, j] != 1:
                path[y+1, j] = 2
                y += 1
        if maze[pos] == "7":
            while y>-1 and path[y-1, j] != 1:
                path[y-1, j] = 2
                y -= 1 
        if ndirection == "J":
            return mark(npos, (0, -1))
        if ndirection == "L":
            return mark(npos, (0, 1))
        if ndirection == "|":
            return mark(npos, (1, 0))
    return 0

def run(pos, direction, step):
    step += 1
    npos = (pos[0] + direction[0], pos[1] + direction[1])
    ndirection = maze[npos]
    path[pos] = 1
    if ndirection == "S" or 0:
        return step
    if direction == (0, -1):
        if ndirection == "L":
            return run(npos, (-1, 0), step)
        if ndirection == "F":
            return run(npos, (1, 0), step)
        if ndirection == "-":
            return run(npos, (0, -1), step)
    if direction == (0, 1):
        if ndirection == "7":
            return run(npos, (1, 0), step)
        if ndirection == "J":
            return run(npos, (-1, 0), step)
        if ndirection == "-":
            return run(npos, (0, 1), step)
    if direction == (-1, 0):
        if ndirection == "7":
            return run(npos, (0, -1), step)
        if ndirection == "F":
            return run(npos, (0, 1), step)
        if ndirection == "|":
            return run(npos, (-1, 0), step)
    if direction == (1, 0):
        if ndirection == "J":
            return run(npos, (0, -1), step)
        if ndirection == "L":
            return run(npos, (0, 1), step)
        if ndirection == "|":
            return run(npos, (1, 0), step)
    return 0

with open('day10.txt', 'r') as file:
    lines = file.readlines()

maze = []
for i in range(len(lines)-1):
    maze.append([j for j in lines[i][:-1]])
maze.append([j for j in lines[-1]])

maze = np.array(maze)

pos = np.where(maze=="S")
pos = (pos[0][0], pos[1][0])
l = len(maze[0])

for direction in [(0,1),(0,-1),(1,0),(-1,0)]:
    path = np.zeros(maze.shape)
    dis = run(pos, direction, 0)
    if dis > 0:
        break

mark(pos, direction)
print(len(np.where(path==0)[0]))
