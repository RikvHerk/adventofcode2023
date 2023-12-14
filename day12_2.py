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
t1 = perf_counter()
for i in range(1):
    s = solve(puzzle[i], instructions[i][:-2], 0, 0)
    
print(len(s), s, perf_counter()-t1)