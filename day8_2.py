import numpy as np

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

with open('day8.txt', 'r') as file:
    lines = file.readlines()
    
lr = [int(i) for i in lines[0][:-1].replace("L", "1").replace("R", "2")]
l = len(lr)

instructions = []
for line in lines[2:]:
    instructions.append([line[0:3], line[7:10], line[12:15]])
instructions = np.array(instructions)

ii = []
for i in instructions[:,0]:
    if i.endswith("A"):
        ii.append(i)

j=0
t=0
periods = []
for i in ii:
    period = 0
    while True:
        i = instructions[np.where(instructions[:,0] == i)[0][0]][lr[j%l]]
        j += 1
        period += 1
        if i.endswith("Z"):
            periods.append(period)
            break

factors = []
for period in periods:
    factors.append(prime_factors(period)) 
    
s = factors[0][1]
for factor in factors:
    s *= factor[0]
    
print(s)
        