import numpy as np

def check(puzzle, instr):
    x = []
    s = 0
    for i in puzzle:
        if i == "#":
            s += 1
        else:
            x.append(s)
            s = 0
    j = 0
    for i in x:
        if i != 0:
            if instr[j] == i:
                j += 1
            else:
                return False
    return True

def solve(puzzle, instr):
    n_1 = sum(instr)
    pos = []
    
    for i in puzzle:
        if i == "?":
            pos.append(i)
            
    n_0 = n_1 - len(pos)
    
    js = [n_1]
    for i in range(n_1):
        sol = ["."]*len(pos)
        for j in js:
            for k in j:
                p = k
                sol[p] = "#"
            
    return

with open("day12.txt", 'r') as inp:
    lines = inp.readlines()

puzzle = []
instructions = []

for line in lines:
    x = line.split(" ")
    puzzle.append([i for i in x[0]])
    instructions.append([int(i) for i in x[1].split(",")])

# s = 0
# for i in range(len(puzzle)):
#     s += solve(puzzle[i], instructions[i])

# print(s)