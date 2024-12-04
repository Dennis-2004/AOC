data = open("day9.txt").readlines()

for i, x in enumerate(data):
    data[i] = []
    data[i].append([int(y) for y in x.strip().split()])

    y = data[i][0]
    while not all([z == 0 for z in y]):
        y = [y[z + 1] - y[z] for z in range(len(y) - 1)]
        data[i].append(y)

def part1(data):
    total = 0
    for x in data:
        A = 0
        for i in range(len(x) - 2, -1, -1):
            A = x[i][-1] + A
        total += A
    return total


def part2(data):
    total = 0
    for x in data:
        A = 0
        for i in range(len(x) - 2, -1, -1):
            A = x[i][0] - A
        total += A
    return total

print(part1(data))
print(part2(data))