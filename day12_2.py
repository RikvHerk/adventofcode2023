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
    if not instr:
        if "#" in puz:
            return np.array([0, 0])
        else:
            return np.array([1, 0])
        
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
                if "#" in puz[start+lseg:]:
                    pass
                elif start+lseg == len(puz):
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
    instructions.append([int(i) for i in x[1].split(",")]*2)

s = 0
c0 = []
c1 = []
c2 = []
c3 = []
c4 = []
t1 = perf_counter()
for i in [11]:#range(1):
    for j in range(len(instructions[i])):
        s = solve(puzzle[i], instructions[i][:j], 0, 0)
        if sum(s) == 0:
            if j>len(instructions)/5:
                break
        else:
            c0.append(np.insert(s,0,j))
    for c in c0:
        for j in [len(instructions[i])-int(c[0])-1]:#range(len(instructions[i])-int(c[0])):
            s1 = solve(puzzle[i], instructions[i][int(c[0]):int(c[0])+j+1], 0, 0)
            s2 = solve([".", "?"] + puzzle[i][1:], instructions[i][int(c[0]):int(c[0])+j+1], 0, 0)
            if sum(s1) == 0 and sum(s2) == 0:
                if j>len(instructions)/5:
                    break
            else:
                s = np.zeros(2)
                s[0] = s2[0]*c[1] + s1[0]*c[2]
                s[1] = s2[1]*c[1] + s1[1]*c[2]
                c1.append(np.insert(s,0,j+int(c[0])+1))
        
                
# for i in [1]:#range(1):
#     for n in c01:
#         if n[1] > 0:
#             for j in range(10):
#                 if j == 0:
#                     s = solve([".", "?"] + puzzle[i][1:], instructions[i], 0, 0)
#                 else:
#                     s = solve([".", "?"] + puzzle[i][1:], instructions[i][-j:]+instructions[i], 0, 0)
#                 if sum(s) == 0:
#                     break
#                 else:
#                     c12.append(np.insert(s,0,j))
#     for k in range(j-1):
#         s = solve(puzzle[i], instructions[i][0:-(k+1)], 0, 0)
#         if sum(s) == 0:
#             break
#         else:
#             c01.append(np.insert(s,0,-k-1))

# s = 0 
# for a in range(len(c01)):
#     z = c01[a][0]
#     for c in range(len(c01)):
#         if c01[c][0] + z == 0:        
#             s += c01[a][2]*np.sum(c01[c][1:])
#             break
#     for b in range(len(c12)):
#         if z + c12[b][0] == 0:
#             s += c01[a][1]*np.sum(c12[b][1:])
#             break


# print(s)