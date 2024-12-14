import re
from math import prod

class bot:
    def __init__(self, data, bounds):
        ints = re.findall(r'-*\d+', data)
        self.x = int(ints[0])
        self.y = int(ints[1])
        self.vx = int(ints[2])
        self.vy = int(ints[3])
        self.w = bounds[0]
        self.h = bounds[1]


    def getPos(self, n=0):
        x = (self.x + n * self.vx) % self.w
        y = (self.y + n * self.vy) % self.h
        return (x, y)


def part1(data, bounds):
    total = [0,0,0,0]
    midx = bounds[0] // 2
    midy = bounds[1] // 2
    for x, y in data:
        if x < midx:
            if y < midy:
                total[0] += 1
            elif y > midy:
                total[1] += 1
        elif x > midx:
            if y < midy:
                total[2] += 1
            elif y > midy:
                total[3] += 1
    return prod(total)


def part2(bots, bounds):
    for i in range(10000):
        grid = [['.'] * bounds[0] for _ in range(bounds[1])]
        poss = [x.getPos(i) for x in bots]

        for x, y in poss:
            grid[y][x] = 'X'

        grid = '\n'.join([''.join(x) for x in grid])

        if 'X'*31 in grid:
            return(i)


data = open('day14.txt').readlines()
bounds = (101, 103)
bots = [bot(x, bounds) for x in data]
data = [x.getPos(100) for x in bots]

print(part1(data, bounds))
print(part2(bots, bounds))