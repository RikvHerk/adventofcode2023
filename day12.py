from time import perf_counter

def check(p, i, c): #puzzle input coordinate
    seg = p[c:c+len(i)]
    for j in range(len(i)):
        if seg[j] == "?" or i[j] == seg[j]:
            continue
        else:
            return False
    return True

def solve(puz, instr, ni, start):
    s = 0
    si = start
    i = instr[ni]
    seg = ["."] + ["#"]*i + ["."]
    while start <= len(puz)-len(seg):
        c = check(puz, seg, start)
        if c:
            if "#" in puz[si:start]:
                return s
            if ni == len(instr) - 1:
                if "#" not in puz[start+len(seg):]:
                    s += 1
                start += 1
                continue
            else:
                sol = solve(puz, instr, ni+1, start + i + 1)
                start += 1 
                if sol > 0:
                    s += sol
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
    instructions.append([int(i) for i in x[1].split(",")])

s = []
t1 = perf_counter()
for i in range(len(puzzle)):
    s.append(solve(puzzle[i], instructions[i], 0, 0))
    
print(s, perf_counter()-t1)