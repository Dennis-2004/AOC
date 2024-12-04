data = open("day6.txt").readlines()

for i, x in enumerate(data):
    x = [int(y) for y in data[i].strip().split(':')[1].split()]
    data[i] = x

def part1(data):
    total = 0
    for i in range(len(data[0])):
        amount = len([x for x in range(data[0][i]) if x * (data[0][i] - x) > data[1][i]])
        if total == 0: total = amount
        else: total *= amount
    return total


def part2(data):
    string = ""
    for x in data[0]:
        string += str(x)
    data[0] = int(string)
    string = ""
    for x in data[1]:
        string += str(x)
    data[1] = int(string)

    return len([x for x in range(data[0]) if x * (data[0] - x) > data[1]])

print(part1(data))
print(part2(data))