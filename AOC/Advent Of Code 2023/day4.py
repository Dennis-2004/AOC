data = open("day4.txt").readlines()

def parseData(data):
    lines = []
    for x in data:
        x = x.strip().split('| ')
        x[0] = x[0].split(':')[1].split()
        x[1] = x[1].split()
        x.append(1)
        lines.append(x)

    return lines

def part1(data):
    total = 0
    for x in data:
        power = 0
        for y in x[0]:
            if y in x[1]:
                power += 1
        if power > 0:
            total += pow(2, power - 1)

    return total

def part2(data):
    for x in range(len(data)):
        power = 0
        for y in data[x][0]:
            if y in data[x][1]:
                power += 1
        for i in range(x + 1, power + 1 +  x):
            if i < len(data):
                data[i][2] += data[x][2]

    return sum([x[2] for x in data])

parsed = parseData(data)

# print(part1(parsed))
print(part2(parsed))