from time import perf_counter

def map(seed, m):
    for line in maps[m]:
        if seed >= line[1] and seed < line[1]+line[2]:
            if m == 6:
                return seed-line[1] + line[0]
            return map(seed-line[1] + line[0], m+1)
    if m == 6:
        return seed
    return map(seed, m+1)

with open("day5.txt", 'r') as inp:
    lines = inp.readlines()

seeds = [int(i) for i in lines[0][7:].split(" ")]
maps = [[],[],[],[],[],[],[]]
n = 0

for line in lines[3:]:
    if not line[0].isdigit():
        n += 0.5
    else:
        maps[int(n)].append([int(i) for i in line.split(" ")])
        
mapped = []

t1 = perf_counter()
for seed in seeds:
    mapped.append(map(seed, 0))
t2 = perf_counter()
print(min(mapped))
print((t2-t1)/20)
