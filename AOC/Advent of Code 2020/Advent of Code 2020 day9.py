lines = open("day9.txt").readlines()
total = 0

for i in range(len(lines)):
    for j in range(25):
        if i+25 