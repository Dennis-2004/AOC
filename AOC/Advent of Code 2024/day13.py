import re
from math import gcd
from collections import defaultdict


def part1(data, part2=0):
    total = 0

    for i in data.keys():
        Ax, Ay = data[i]['A']
        Bx, By = data[i]['B']
        Px, Py = data[i]['P']
        Px, Py = Px + part2, Py + part2
        d = Ax * By - Bx * Ay
        a = Px * By - Py * Bx
        b = Px * Ay - Py * Ax

        if any([a % d, b % d, not d]):
            continue

        a, b = a // d, -b // d

        total += 3 * a + b if (max(a, b) <= 100 or part2) else 0
    return total

data = open('day13.txt').read()
values = re.findall(r'\d+', data)
games = defaultdict(dict)

for i in range(int(len(values)/6)):
    games[i]['A'] = (int(values[i*6]), int(values[i*6+1]))
    games[i]['B'] = (int(values[i*6+2]), int(values[i*6+3]))
    games[i]['P'] = (int(values[i*6+4]), int(values[i*6+5]))

print(part1(games))
print(part1(games, 10000000000000))