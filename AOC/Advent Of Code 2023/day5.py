import time

data = open("day5.txt").readlines()
maps = ["seed-to-soil map:\n", "soil-to-fertilizer map:\n", "fertilizer-to-water map:\n", "water-to-light map:\n", "light-to-temperature map:\n", "temperature-to-humidity map:\n", "humidity-to-location map:\n"]

def parseData(data):
    parsed = []
    parsed.append([int(x) for x in data[0].strip().split(': ')[1].split()])
    for i, x in enumerate(maps, 1):
        index = data.index(x)
        parsed.append([])

        while index + 1 < len(data):
            index += 1
            if data[index] == "\n": break
            parsed[i].append([int(y) for y in data[index].strip().split()])

    return parsed


def nextMap(map, seeds):
    next = []
    for seed in seeds:
        changed = False
        for rule in map:
            if seed[0] >= rule[1] and seed[0] + seed[1] <= rule[1] + rule[2]:
                next.append([rule[0] + (seed[0] - rule[1]), seed[1]])
                changed = True
                break
            elif seed[0] + seed[1] - 1 > rule[1] and seed[0] + seed[1] <= rule[1] + rule[2]:
                inside = [rule[1], seed[1] - (rule[1] - seed[0])]
                outside = [seed[0], (rule[1] - seed[0])]
                next.append([rule[0] + (inside[0] - rule[1]), inside[1]])
                seeds.append(outside)
                changed = True
                break
            elif seed[0] >= rule[1] and  seed[0] < rule[1] + rule[2]:
                inside = [seed[0], seed[1] - ((seed[0]+ seed[1]) - (rule[1] + rule[2]))]
                outside = [inside[0] + inside[1] , (seed[0]+ seed[1]) - (inside[0] + inside[1])]
                next.append([rule[0] + (inside[0] - rule[1]), inside[1]])
                seeds.append(outside)
                changed = True
                break
        if not changed: next.append(seed)

    return next


def part1(data):
    location = []
    for seed in data[0]:
        point = seed
        for map in data[1:]:
            for rule in map:
                if point >= rule[1] and point < rule[1] + rule[2]:
                    point = rule[0] + (point - rule[1])
                    break
        location.append(point)
    return min(location)


def part2(data):
    seeds = [ [data[0][x], data[0][x + 1]] for x in range(0, len(data[0]), 2)]
    for map in data[1:]:
        seeds = nextMap(map, seeds)

    return min([x[0] for x in seeds])

data = parseData(data)
print(part1(data))

start = time.time()
print(part2(data))
end = time.time()
print(end - start)