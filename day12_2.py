from time import perf_counter
import numpy as np

def check(p, i, c): #puzzle input coordinate
    seg = p[c:c+len(i)]
    for j in range(len(i)):
        if seg[j] == "?" or i[j] == seg[j]:
            continue
        else:
            return False
    return True

def solve(puz, instr, ni, start):
    s = np.zeros(2)
    si = start
    i = instr[ni]
    seg = ["."] + ["#"]*i + ["."]
    lseg = i+2
    while start <= len(puz)-lseg:
        if check(puz, seg, start):
            if "#" in puz[si:start]:
                return s
            if ni == len(instr) - 1:
                if start+lseg == len(puz):
                    s[1] += 1
                else:
                    s[0] += 1
                start += 1
                continue
            else:
                s += solve(puz, instr, ni+1, start + i + 1)
                start += 1
        else:
            start += 1
    return s


with open("day12.txt", 'r') as inp:
    lines = inp.readlines()
puzzle = []
instructions = []
# lines = ['?#??#??#..#?#???. 1,4,1,1,2']
for line in lines:
    x = line.split(" ")
    puzzle.append(["."] + [i for i in x[0]] + ["."])
    instructions.append([int(i) for i in x[1].split(",")])


s = 0
normal = []
extra = []
t1 = perf_counter()
for i in [1]:#range(1):
    for j in range(10):
        s = solve(puzzle[i], instructions[i]+instructions[i][0:j], 0, 0)
        if sum(s) == 0:
            break
        else:
            normal.append(np.insert(s,0,j))
for i in [1]:#range(1):
    for n in normal:
        if n[1] > 0:
            for j in range(10):
                if j == 0:
                    s = solve([".", "?"] + puzzle[i][1:], instructions[i], 0, 0)
                else:
                    s = solve([".", "?"] + puzzle[i][1:], instructions[i][-j:]+instructions[i], 0, 0)
                if sum(s) == 0:
                    break
                else:
                    extra.append(np.insert(s,0,j))
    for k in range(j-1):
        s = solve(puzzle[i], instructions[i][0:-(k+1)], 0, 0)
        if sum(s) == 0:
            break
        else:
            normal.append(np.insert(s,0,-k-1))

s = 0 
for a in range(len(normal)):
    z = normal[a][0]
    for c in range(len(normal)):
        if normal[c][0] + z == 0:        
            s += normal[a][2]*np.sum(normal[c][1:])
            break
    for b in range(len(extra)):
        if z + extra[b][0] == 0:
            s += normal[a][1]*np.sum(extra[b][1:])
            break


print(s)