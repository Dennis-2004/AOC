from collections import deque

def part1(grid):
    start = (0, 0)
    end = (70, 70)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, [])])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()
        if (x, y) == end: return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and not grid[ny][nx] and (nx, ny) not in visited:
                visited.add((nx, ny))
                dstep = steps + [(nx, ny)]
                queue.append(((nx, ny), dstep))

    return -1


def part2(grid, path, data):
    for x in data[1024:]:
        x, y = x.split(',')
        grid[int(y)][int(x)] = True

        if (int(x), int(y)) in path:
            path = part1(grid)

            if path == -1:
                return int(x), int(y)

data = open("data/day18.txt").readlines()

grid = [[False] * 71 for _ in range(71)]
for x in data[:1024]:
    x, y = x.split(',')
    grid[int(y)][int(x)] = True

path = part1(grid)
print(len(path))
print(part2(grid, path, data))