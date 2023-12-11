import numpy as np

inp = np.genfromtxt("day2.txt", dtype = str, delimiter=':')

r = 12
g = 13
b = 14

s = 0

for n, i in enumerate(inp[:,1]):
    valid = True
    for j in i.replace(" ", "").replace(";", ",").split(","):
        if 'd' in j:
            if int(j[0:-3]) > r:
                valid = False
                break
        elif 'g' in j:
            if int(j[0:-5]) > g:
                valid = False
                break
        elif 'u' in j:
            if int(j[0:-4]) > b:
                valid = False
                break
    if valid:
        s += 1 + n
        
print(s)

s = 0

for i in inp[:,1]:
    r = 0 
    g = 0
    b = 0
    for j in i.replace(" ", "").replace(";", ",").split(","):
        if 'd' in j:
            if int(j[0:-3]) > r:
                r = int(j[0:-3])
        elif 'g' in j:
            if int(j[0:-5]) > g:
                g = int(j[0:-5])
        elif 'u' in j:
            if int(j[0:-4]) > b:
                b = int(j[0:-4])
    s += r * g * b

print(s)
            