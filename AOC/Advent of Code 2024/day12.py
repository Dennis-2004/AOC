def parts(regions, data):
    part1 = 0
    part2 = 0
    for region in regions:
        perimeter = 0
        sides = 0
        for x, y in region:
            subset = [[(ix, iy) for ix in range(x - 1, x + 2)] for iy in range(y - 1, y + 2)]
            for _ in range(4):
                if subset[1][0] not in region and subset[0][1] not in region:
                    sides += 1
                elif subset[1][0] in region and subset[0][1] in region:
                    if subset[0][0] not in region:
                        sides += 1
                subset = [row[::-1] for row in [list(row) for row in zip(*subset)]]
            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dx = x + dx
                dy = y + dy
                if (dx, dy) not in region:
                    perimeter += 1
        part1 += perimeter * len(region)
        part2 += sides * len(region)

    return part1, part2


def getRegions(data):
    w = len(data[0]) - 1
    h = len(data)
    garden = sum([[(x, y) for x in range(w)]for y in range(h)],[])
    regions = []

    while len(garden):
        crop = garden.pop()
        region = [crop]
        stack = [crop]
        crop = data[crop[1]][crop[0]]

        while len(stack):
            x, y = stack.pop()

            for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dx = x + dx
                dy = y + dy
                if dx < 0 or dx >= w: continue
                if dy < 0 or dy >= h: continue
                if data[dy][dx] == crop and (dx, dy) not in region:
                    region.append((dx, dy))
                    stack.append((dx, dy))
                    garden.remove((dx, dy))
        regions.append(region)
    return regions


data = open('day12.txt').readlines()
regions = getRegions(data)
part1, part2 = parts(regions, data)
print(part1)
print(part2)