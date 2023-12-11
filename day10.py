import numpy as np

import sys

sys.setrecursionlimit(100000)

def run(pos, direction, step):
    step += 1
    npos = (pos[0] + direction[0], pos[1] + direction[1])
    ndirection = maze[npos]
    if ndirection == "S":
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
l = 0

for direction in [(0,1),(0,-1),(1,0),(-1,0)]:
    dis = run(pos, direction, 0)
    if dis > 0:
        break
    
print(dis/2)