import numpy as np

with open('day8.txt', 'r') as file:
    lines = file.readlines()
    
lr = [int(i) for i in lines[0][:-1].replace("L", "1").replace("R", "2")]
l = len(lr)

instructions = []
for line in lines[2:]:
    instructions.append([line[0:3], line[7:10], line[12:15]])
instructions = np.array(instructions)

i = "AAA"
j = 0 
while i != "ZZZ":
    i = instructions[np.where(instructions[:,0] == i)[0][0]][lr[j%l]]
    j += 1

print(j)