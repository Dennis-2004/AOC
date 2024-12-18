orth = {'>': (1, 0), 'v': (0, 1), '<': (-1, 0), '^': (0, -1)}

def expandGraph(map):
    w, h = len(map[0]), len(map)
    for y in range(h):
        for x in range(w):
            if map[y][x] == '.':
                map[y][x] = '..'
            if map[y][x] == 'O':
                map[y][x] = '[]'
            if map[y][x] == '#':
                map[y][x] = '##'
            if map[y][x] == '@':
                map[y][x] = '@.'
        map[y] = list(''.join(map[y]))
    return map


def part1(map, moves, bot, part2=False):
    total = 0
    bx, by = bot
    bx = bx*2 if part2 else bx
    for move in moves:
        dx, dy = orth[move]

        boxes = [(bx, by)]
        x, y = bx+dx, by+dy
        checks = [[x, y]]
        while not all([map[y][x] == '.' for x, y in checks]) and not any([map[y][x] == '#' for x, y in checks]):
            next = set()
            for x, y in checks:
                if map[y][x] == 'O':
                    next.add((x+dx, y+dy))
                    boxes.append((x, y))
                if map[y][x] == '[':
                    next.add((x+dx, y+dy))
                    if (x, y) not in boxes: boxes.append((x, y))
                    if dy:
                        next.add((x+dx+1, y+dy))
                        if (x+1, y) not in boxes: boxes.append((x+1, y))
                if map[y][x] == ']':
                    next.add((x+dx, y+dy))
                    if (x, y) not in boxes: boxes.append((x, y))
                    if dy:
                        next.add((x+dx-1, y+dy))
                        if (x-1, y) not in boxes: boxes.append((x-1, y))
            x, y = x+dx, y+dy
            checks = list(next)
        if any([map[y][x] == '#' for x, y in checks]):
            continue

        for i in range(1, len(boxes)+1):
            x, y = boxes[-i]
            map[y+dy][x+dx] = map[y][x]
            map[y][x] = '.'
        bx, by = x+dx, y+dy

    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] in ['O', '[']:
                total += 100*y + x
    return total

bounds = [51, 11, 8]
x = bounds[0]
data = open('data/day15.txt').read()
bot = (data.find('@') % x, data.find('@') // x)
data = data.split('\n\n')
map = [list(x) for x in data[0].split()]
moves = ''.join(data[1].split())

print(part1(map, moves, bot))
map = expandGraph(map)
print(part1(map, moves, bot, True))