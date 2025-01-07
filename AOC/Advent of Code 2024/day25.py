import numpy as np


def parse(data):
    keys = []
    locks = []

    for com in data:
        com = com.split('\n')
        array = None
        if com[0] == '#####':
            array = locks
            com = com[1:]
        else:
            array = keys
            com = com[:-1]
        pins = np.zeros(len(com[0]))

        for i in com:
            pins += np.array([1 if j == '#' else 0 for j in i])

        array.append(pins)
    return keys, locks


def part1(keys, locks):
    total = 0

    for lock in locks:
        for key in keys:
            attempt = key + lock
            if not any([i for i in attempt if i > 5]):
                total += 1

    return total

keys, locks = parse(open('data/day25.txt').read().split('\n\n'))
print(part1(keys, locks))