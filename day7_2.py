card_value = {"A": 22, "K": 21, "Q": 20, "J": 10, "T": 19, "9": 18, "8": 17, "7": 16, "6": 15, "5": 14, "4": 13, "3": 12, "2": 11}

def find_type(hand):
    values = {}
    nvalues = {"A": 0, "K": 0, "Q": 0, "J": 0, "T": 0, "9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0}
    for i in hand:
        values[i] = 1
        nvalues[i] += 1
    l = len(values)
    n = "".join([str(card_value[i]) for i in hand])
    if "J" in values:
        js = nvalues["J"]
        if js == 5:
            return int("7" + n)
        del nvalues["J"]
        nvalues[max(nvalues, key=nvalues.get)] += js
        l -= 1
    if l == 5:
        return int("1" + n)
    if l == 4:
        return int("2" + n)
    if l == 3:
        for key, value in nvalues.items():
            if value == 2:
                return int("3" + n)
            if value == 3:
                return int("4" + n)    
    if l == 2:
        for key, value in nvalues.items():
            if value == 3:
                return int("5" + n)    
            if value == 4:
                return int("6" + n)       
    if l == 1:
        return int("7" + n)
           
with open('day7.txt', 'r') as file:
    lines = file.readlines()

hands = []
bids = []

for line in lines:
    line = line.split(" ")
    bids.append(int(line[1]))
    hands.append([i for i in line[0]])
    
scores = []
for index, hand in enumerate(hands):
    scores.append([index, find_type(hand)])

n_hands = len(hands)
for i in range(n_hands):
    for j in range(n_hands-i-1):
        if scores[i][1] > scores[i+j+1][1]:
            scores[i][0] += 1
            scores[i+j+1][0] -= 1 

s = 0
for i in range(n_hands):
    s += bids[i]*(scores[i][0]+1)
    
print(s)