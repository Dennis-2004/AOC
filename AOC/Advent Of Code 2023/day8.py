import math

data = open("day8.txt").readlines()
key = data[0].strip()
path = {}
way = ['L', 'R']

for x in range(2, len(data)):
    y = data[x].strip().split(" = ")
    path[y[0]] = [y[1].split(", ")[0].removeprefix('('), y[1].split(", ")[1].removesuffix(')')]

def part1(path):
    total = 0
    curr = 'AAA'
    while True:
        curr = path[curr][way.index(key[total%len(key)])]
        total += 1
        if curr == 'ZZZ':
            return total


def part2(path):
    curr = [x for x in path.keys() if x[2] == 'A']
    moves = []
    for x in curr:
        total = 0
        while x[2] != 'Z':
            x = path[x][way.index(key[total%len(key)])]
            total += 1
        moves.append(total)
    return math.lcm(*moves)

print(part1(path))
print(part2(path))