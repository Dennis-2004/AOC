lines = open("day7.txt").readlines()
total = []
check = ["shiny gold"]
data = {}

for i in range(len(lines)):
    rule = lines[i].split()
    temp = []
    for j in range(int(len(rule)/4)):
        if j != 0:
            temp.append(rule[j*4+1] + " " + rule[j*4+2])
    data[rule[0] + " " + rule[1]] = temp

while len(check) != 0:
    temp = []
    for i in data.keys():
        for j in range(len(check)):
            if check[j] in data[i] and not i in total:
                temp.append(i)
                total.append(i)
    check = temp

total.sort()
print(len(total))