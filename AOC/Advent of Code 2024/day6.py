import re

def part1(map):
    width = len(map.split('\n')[0]) + 1
    height = len(map.split('\n'))
    dir = 0
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    pos = map.index('^')
    pos = (pos % width, int(pos / width))
    obs = [(i % width, int(i / width)) for i, x in enumerate(map) if x == '#']
    paths = []
    loop = False

    while 1:
        if dir == 0:
            ob = [ob for ob in obs if ob[0] == pos[0] and ob[1] < pos[1]]
            ob.sort(key=lambda ob: -ob[1])
        elif dir == 1:
            ob = [ob for ob in obs if ob[1] == pos[1] and ob[0] > pos[0]]
            ob.sort(key=lambda ob: ob[0])
        elif dir == 2:
            ob = [ob for ob in obs if ob[0] == pos[0] and ob[1] > pos[1]]
            ob.sort(key=lambda ob: ob[1])
        elif dir == 3:
            ob = [ob for ob in obs if ob[1] == pos[1] and ob[0] < pos[0]]
            ob.sort(key=lambda ob: -ob[0])

        if len(ob) == 0:
            if dir == 0:
                paths.append((pos, (pos[0], 0)))
            if dir == 1:
                paths.append((pos, (width - 2, pos[1])))
            if dir == 2:
                paths.append((pos, (pos[0], height - 1)))
            if dir == 3:
                paths.append((pos, (0, pos[1])))
            break

        ob = ob[0]
        new_pos = (ob[0] + dirs[dir][0], ob[1] + dirs[dir][1])

        if (pos, new_pos) in paths:
            loop = True
            break

        paths.append((pos, new_pos))
        pos = new_pos
        dir = (dir + 1) % 4

    visited = set([])
    for path in paths:
        start, end = path
        for x in range(min(start[0], end[0]), max(start[0], end[0])+1):
            for y in range(min(start[1], end[1]), max(start[1], end[1])+1):
                visited.add((x, y))
    return visited, loop


def part2(map, visited):
    total = 0
    width = len(map.split('\n')[0]) + 1
    pos = map.index('^')

    for loc in visited:
        x, y = loc
        loc = y * width + x
        if loc != pos:
            new = map[:loc] + '#' + map[loc+1:]
            _, loop = part1(new)
            if loop:
                total += 1
    return total

map = open("data/day6.txt").read()
visited, _ = part1(map)
print(len(visited))
print(part2(map, visited))

