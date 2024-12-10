import numpy as np

data = open("day2.txt").readlines()
colours = ['red', 'green', 'blue']
cubes = [-12, -13, -14]

def prepareLines(x):
    x = x.strip().split("; ")
    id = int(x[0].split(': ')[0].split()[1])
    x[0] = x[0].split(': ')[1]
    x = [a.split(', ') for a in x]

    return x, id

def part1(lines):
    sorted = []
    for x in lines:
        x, id = prepareLines(x)
        game = []

        for y in x:
            round = [0, 0, 0]
            for z in y:
                for i in range(3):
                    if colours[i] in z:
                        round[i] = int(z.split()[0])
            round = [x + y for x, y in zip(round, cubes)]
            game.append(any([n > 0 for n in round]))
        if not any(game): sorted.append(id)
    return sum(sorted)

def part2(lines):
    total = 0
    for x in lines:
        x, _ = prepareLines(x)
        game = [0, 0, 0]
        for y in x:
            for z in y:
                for i in range(3):
                    if colours[i] in z:
                        game[i] = max(game[i], int(z.split()[0]))
        total += np.prod(game)

    return total

print(part1(data))
print(part2(data))