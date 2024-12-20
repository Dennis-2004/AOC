orth = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_path(map, start, end, wall='#'):
    visited = set()
    stack = [(start, [(start, 0)])]

    while stack:
        pos, path = stack.pop()
        x, y = pos
        visited.add((x, y))

        for dx, dy in orth:
            if (x+dx, y+dy) == end:
                return path + [((x+dx, y+dy), path[-1][1] + 1)]
            elif map[y+dy][x+dx] != wall and (x+dx, y+dy) not in visited:
                new_path = path + [((x+dx, y+dy), path[-1][1] + 1)]
                stack.append(((x+dx, y+dy), new_path))


def part1(map, path):
    dir = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    path_dict = {}
    walls = set()
    total = 0

    for pos, step in path:
        path_dict[pos] = step

    path = path_dict.keys()

    for x, y in path:
        for i in range(4):
            dx, dy = orth[i]
            ddx, ddy = dir[i]

            if (x+dx, y+dy) not in walls and map[y+dy][x+dx] == '#':
                walls.add((x+dx, y+dy))
                if (x+ddx, y+ddy) in path_dict:
                    if path_dict[(x+ddx, y+ddy)] - path_dict[(x, y)] >= 102:
                        total += 1

    return total


def part2(map, path):
    path_dict = {}
    total = 0

    for pos, step in path:
        path_dict[pos] = step

    path = list(path_dict.keys())

    for i in range(len(path)):
        x1, y1 = path[i]

        for j in range(i+1, len(path)):
            x2, y2 = path[j]

            distance = abs(x2 - x1) + abs(y2 - y1)
            if distance <= 20:
                if path_dict[(x2, y2)] - path_dict[(x1, y1)] - distance >= 100:
                    total += 1

    return total


data = open('data/day20.txt').read()

start = data.find('S')
end = data.find('E')
map = [list(x.strip()) for x in data.split('\n')]
start = (start%(len(map[0])+1), start//(len(map[0])+1))
end = (end%(len(map[0])+1), end//(len(map[0])+1))
path = get_path(map, start, end)

print(part1(map, path))
print(part2(map, path))