import numpy as np

def part1(left, right):
    total = 0
    for l, r in tuple(zip(left, right)):
        total += abs(l-r)
    return total


def part2(left, right):
    total = 0

    unique, counts = np.unique(np.array(right), return_counts=True)

    amount = dict(zip(unique, counts))
    print(amount)

    print(amount)

    for x in left:
        if x in amount:
            total += int(x) * amount[x]

    return total

lines = open("data/day1.txt").readlines()

left = []
right = []
for line in lines:
    L, R = line.split()
    left.append(int(L))
    right.append(int(R))

left = sorted(left)
right = sorted(right)

print(part2(left, right))