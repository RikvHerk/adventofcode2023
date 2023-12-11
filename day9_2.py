def extrapolate(seq):
    dif = []
    for i in range(len(seq)-1):
        dif.append(seq[i+1]-seq[i])
    if all([i == 0 for i in dif]):
        return seq[0]
    else:
        return seq[0] - extrapolate(dif)

with open('day9.txt', 'r') as file:
    lines = file.readlines()
    
for i in range(len(lines)):
    lines[i] = [int(j) for j in lines[i].split(" ")]

s = 0

for line in lines:
    s += extrapolate(line)

print(s)