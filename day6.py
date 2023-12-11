def distance(T, D):
    return round((T**2-4*D)**(1/2))

with open("day6.txt", 'r') as file:
    times = [int(i) for i in file.readline()[13:].split("     ")]
    distances = [int(i) for i in file.readline()[12:].split("   ")]

s = 1

for i in range(4):
    s *= distance(times[i], distances[i]) 
    
print(s)