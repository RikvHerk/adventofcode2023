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

def inverted_map(seed, m):
    for line in maps[m]:
        if seed >= line[0] and seed < line[0]+line[2]:
            if m == 0:
                return seed-line[0] + line[1]
            return inverted_map(seed-line[0] + line[1], m-1)
    if m == 0:
        return seed
    return inverted_map(seed, m-1)

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
        
seed = 0
x = 0
r = int(len(seeds)/2)

while x == 0:
    mapped = inverted_map(seed, 6)
    for i in range(r):
        if mapped >= seeds[2*i] and mapped < seeds[2*i] + seeds[2*i+1]:
            x = 1
            break
    seed += 1
            
print(seed-1)

