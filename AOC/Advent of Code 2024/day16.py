import numpy as np
from collections import defaultdict
import time

def drawPaths(data, paths):
    start = data.find('S')
    target = data.find('E')
    w = len(data.split('\n')[0]) + 1
    h = len(data.split('\n'))
    maze = ''
    grid = [list(x.strip()) for x in data.split('\n')]

    for path in paths:
        for pos, _ in path:
            grid[pos // w][pos % w] = 'O'
    grid[start // w][start % w] = 'S'
    grid[target // w][target % w] = 'E'

    maze = '\n'.join(''.join(x) for x in grid)
    print(maze == data)
    print(maze)


def part1(data):
    w = len(data.split('\n')[0]) + 1
    h = len(data.split('\n'))
    orth = [1, -w, -1, w]

    start = data.find('S')
    target = data.find('E')

    stack = [(start, 0, 0, [(start, 0)])]
    visited = defaultdict(dict)
    best_score = float('inf')
    best_paths = []

    while stack:
        pos, score, dir, path = stack.pop()

        if score > best_score:
            continue

        if pos == target:
            if score < best_score:
                best_score = score
                best_paths = [path]
            elif score == best_score:
                best_paths.append(path)
            continue

        if dir not in visited[pos] or visited[pos][dir] >= score:
            visited[pos][dir] = score

            for i in range(4):
                new_pos = pos + orth[i]
                if data[new_pos] != '#' and (i not in visited[new_pos] or visited[new_pos][i] >= score):
                    new_score = score + 1 if i == dir else score + 1001
                    stack.append((new_pos, new_score, i, path + [(new_pos, i)]))

        stack = sorted(stack, key=lambda x: x[1])

    total_seats = len(list(set([x for x, _ in sum(best_paths, [])])))
    return best_score, total_seats


start = time.time()
data = open('data/day16.txt').read()
best_score, total_seats = part1(data)

print(best_score)
print(total_seats)
print(time.time() - start)
# drawPaths(data, best_paths)
