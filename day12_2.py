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

def solve(puz, instrp, ni, start):
    last = instrp[-1]
    instr = instrp[:-1]
    s = np.zeros(15)
    if len(instr)<1:
        if "#" in puz:
            q = 0
            for j in range(len(puz)):
                if puz[j] != "#":
                    q += 1
                else:
                    break
            if len(puz) - q <= last:
                if not "." in puz[q+1:-1]:    
                    s[len(puz) - q -1] += 1
            return s
        else:
            q = 0
            for j in np.arange(-2, -len(puz), -1):
                if puz[j] == "?":
                    q += 1
                else:
                    break
            if q < last:
                s[q+1] = 1
                return s
            else:
                s[last] = 1
                return s
            s[1] = 1
            return s 
    si = start
    i = instr[ni]
    seg = ["."] + ["#"]*i + ["."]
    lseg = i+2
    while start <= len(puz)-lseg:
        if check(puz, seg, start):
            if "#" in puz[si:start]:
                return s
            if ni == len(instr) - 1:
                b = 0
                for h in puz[start+lseg:]:
                    if h == "#":
                        b += 1
                if b > last:
                    pass
                elif start+lseg == len(puz):
                    s[0] += 1
                else:
                    end = puz[start+lseg:-1]
                    if "#" in puz[start+lseg:-last]:
                        start += 1
                        continue
                    q = 0
                    for j in np.arange(-1, -len(end)-1, -1):
                        if end[j] != ".":
                            q += 1
                        else:
                            break
                    if q < last:
                        if "#" in end[:(-1 if q == 0 else -q)]:
                            start += 1
                            continue
                        s[q+1] += 1
                    else:
                        s[last] += 1
                start += 1
                continue
            else:
                s += solve(puz, instrp, ni+1, start + i + 1)
                start += 1
        else:
            start += 1
    return s


with open("day12.txt", 'r') as inp:
    lines = inp.readlines()
puzzle = []
instructions = []

for line in lines:
    x = line.split(" ")
    puzzle.append(["."] + [i for i in x[0]] + ["."])
    instructions.append([int(i) for i in x[1].split(",")]*5 + [0])

ss = []
t0 = perf_counter()
for i in range(len(puzzle)):
    t1 = perf_counter()
    c0 = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    for j in range(len(instructions[i])):
        s = solve(puzzle[i], instructions[i][:j+1], 0, 0)
        if sum(s) != 0:
            c0.append(np.insert(s,0,j))
    for c in c0:
        for j in range(len(instructions[i])-int(c[0])):
            ninstr = instructions[i][int(c[0]):int(c[0])+j+1]
            for n, k in enumerate(c[1:]):
                if k > 0:
                    s = solve(["."] + ["?"]*n + puzzle[i][1:], ninstr, 0, 0)
                    if sum(s) != 0:
                        c1.append(np.insert(k*s,0,j+int(c[0])))
    for c in c1:
        for j in range(len(instructions[i])-int(c[0])):
            ninstr = instructions[i][int(c[0]):int(c[0])+j+1]
            for n, k in enumerate(c[1:]):
                if k > 0:
                    s = solve(["."] + ["?"]*n + puzzle[i][1:], ninstr, 0, 0)
                    if sum(s) != 0:
                        c2.append(np.insert(k*s,0,j+int(c[0])))
    for c in c2:
        for j in range(len(instructions[i])-int(c[0])):
            ninstr = instructions[i][int(c[0]):int(c[0])+j+1]
            for n, k in enumerate(c[1:]):
                if k > 0:
                    s = solve(["."] + ["?"]*n + puzzle[i][1:], ninstr, 0, 0)
                    if sum(s) != 0:
                        c3.append(np.insert(k*s,0,j+int(c[0])))
    for c in c3:
        for j in [len(instructions[i])-int(c[0])-1]:#range(len(instructions[i])-int(c[0])):
            ninstr = instructions[i][int(c[0]):int(c[0])+j+2]
            if not ninstr:
                continue
            for n, k in enumerate(c[1:]):
                if k > 0:
                    s = solve(["."] + puzzle[i][(-1 if n == 0 else -n):-1] + ["?"]*(0 if n == 0 else 1) + puzzle[i][1:], ninstr, 0, 0)
                    if sum(s) != 0:
                        c4.append(np.insert(k*s,0,j+int(c[0])+1))
    s = 0                   
    for c in c4:
        s += sum(c[1:])
    ss += s
    print(i, s, perf_counter()-t1)
print(ss, perf_counter()-t0)