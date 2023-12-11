def distance(T, D):
    return int((T**2-4*D)**(1/2))

with open("day6.txt", 'r') as file:
    times = int(file.readline()[13:].replace(" ", ""))
    distances = int(file.readline()[12:].replace(" ", ""))

s = distance(times, distances) 
    
print(s)