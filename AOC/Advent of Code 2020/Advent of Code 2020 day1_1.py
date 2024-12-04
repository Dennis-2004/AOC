lines = open("day1.txt").readlines()
data = []

for i in range(len(lines)):
    t = int(lines[i])
    data.append(t)


for i in range(len(data)):
    for j in range(len(data)):
        for k in range(len(data)):
            if data[i] + data[j] + data[k] == 2020:
                print(data[i] * data[j] * data[k])
                exit()