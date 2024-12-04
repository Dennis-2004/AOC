import numpy as np

def part1(data):
    total = 0
    for i in range(len(data)):
        asc = sorted(data[i])
        desc = sorted(data[i], reverse=True)

        if data[i] == asc or data[i] == desc:
            for j in range(1, len(data[i])):
                if abs(data[i][j] - data[i][j-1]) not in list(range(1, 4)):
                    break
                if j == len(data[i]) - 1:
                    total += 1
    return total


def part2(data):
    total = 0
    good = []
    for i in range(len(data)):
        asc = sorted(data[i])
        desc = sorted(data[i], reverse=True)

        if data[i] == asc or data[i] == desc:
            for j in range(1, len(data[i])):
                if abs(data[i][j] - data[i][j-1]) not in list(range(1, 4)):
                    break
                if j == len(data[i]) - 1:
                    total += 1
                    good.append(data[i])

    bad = [x for x in data if x not in good]

    for i in range(len(bad)):
        fixed = False
        for j in range(len(bad[i])):
            if fixed:
                break

            temp = bad[i].copy()
            temp.pop(j)
            asc = sorted(temp)
            desc = sorted(temp, reverse=True)

            if temp == asc or temp == desc:
                for k in range(1, len(temp)):
                    if abs(temp[k] - temp[k-1]) not in list(range(1, 4)):
                        break
                    if k == len(temp) - 1:
                        fixed = True
                        total += 1

    return total

lines = open("day2.txt").readlines()
data = []

for line in lines:
    data.append([int(x) for x in line.split()])

print(part1(data))
print(part2(data))