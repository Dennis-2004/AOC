lines = open("day7.txt").readlines()
data = {}
emptyBags = []
total = 0

for i in range(len(lines)):
    rule = lines[i].split()
    temp = {}
    for j in range(int(len(rule)/4)):
        if j != 0:
            temp[rule[j*4+1] + " " + rule[j*4+2]] = int(rule[j*4])
    data[rule[0] + " " + rule[1]] = temp

for i in data.keys():
    if len(data[i]) == 0:
        emptyBags.append(i)

bags = {"shiny gold": 1}

while len(bags) != 0:
    temp = {}
    for i in bags.keys():
        total += bags[i]
        for j in data[i].keys():
            temp[j] = data[i][j] * bags[i]
    bags = temp

print(total - 1)