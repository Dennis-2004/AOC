def part1(map, part2=False):
    total = 0
    starts = sum([[(x, y) for x in range(len(map[0])) if map[y][x] == 0] for y in range(len(map))], [])

    for start in starts:
        ends = 0
        stack = []
        visited = []
        stack.append(start)
        while len(stack):
            x, y = stack.pop()
            if not part2:
                visited.append((x, y))
            for dx, dy in [(-1, 0), (0,1), (1, 0), (0, -1)]:
                if 0 <= y+dy < len(map) and 0 <= x+dx < len(map[0]):
                    if map[y + dy][x + dx] - map[y][x] == 1 and (x + dx, y + dy) not in visited:
                        stack.append((x + dx, y + dy))
                        if map[y + dy][x + dx] == 9:
                            ends += 1
        total += ends
    return total

map = open("data/day10.txt").readlines()
for x in range(len(map)):
    map[x] = [int(i) for i in map[x].split()[0]]

print(part1(map))
print(part1(map, True))