from collections import defaultdict

def part1(map, freqs, max=0):
    antinodes = set([])
    h = len(map)
    w = len(map[0]) - 1
    for freq in freqs:
        n = len(freqs[freq])
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not max:
                    antinodes.add(freqs[freq][i])
                    antinodes.add(freqs[freq][j])
                res = 1
                dx = freqs[freq][i][0] - freqs[freq][j][0]
                dy = freqs[freq][i][1] - freqs[freq][j][1]
                while 1:
                    added = 0
                    n1 = (freqs[freq][i][0] + (dx *  res), freqs[freq][i][1] + (dy *  res))
                    n2 = (freqs[freq][j][0] - (dx *  res), freqs[freq][j][1] - (dy *  res))
                    if 0 <= n1[0] < w and 0 <= n1[1] < h:
                        antinodes.add(n1)
                        added += 1
                    if 0 <= n2[0] < w and 0 <= n2[1] < h:
                        antinodes.add(n2)
                        added += 1
                    if not added or res == max:
                        break
                    res += 1
    return len(antinodes)


map = open("data/day8.txt").readlines()
freqs = defaultdict(list)

for y in range(len(map)):
    for x in range(len(map[0]) - 1):
        if map[y][x] != '.':
            freqs[map[y][x]].append((x, y))

print(part1(map, freqs, max=1))
print(part1(map, freqs))