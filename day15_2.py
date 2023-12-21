import numpy as np

def hash(i):
    s = 0
    for j in i:
        s += ord(j)
        s *= 17
        s %= 256
    return s

inp = np.genfromtxt("day15.txt", dtype=str, delimiter=",")

boxes = []
for i in range(256):
    boxes.append([])
    
for i in inp:
    p = 0
    for j in i:
        if j in ["=", "-"]:
            op = j
            break
        p += 1
    
    label = i[0:p]
    box = hash(label)
    if op == "=":
        f = False
        lens = i[p+1:]
        for j, b in enumerate(boxes[box]):
            if label == b[0]:
                boxes[box][j] = [label, lens]
                f = True
                break
        if not boxes[box] or not f:
            boxes[box].append([label, lens])
    if op == "-":
        for b in boxes[box]:
            if label == b[0]:
                boxes[box].remove(b)

s = 0
for i, box in enumerate(boxes):
    for j, b in enumerate(box):
        s += (i+1)*(j+1)*int(b[1])

print(s)