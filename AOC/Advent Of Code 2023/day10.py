import networkx as nx
import numpy as np
from skimage.segmentation import flood_fill

data = open("day10.txt").readlines()

data = [list(x.strip()) for x in data]
directions = {'|': [[1,0], [-1,0]], '-': [[0,1], [0,-1]], 'L': [[-1,0],[0,1]], 'J': [[-1,0],[0,-1]], '7': [[1,0],[0,-1]], 'F': [[1,0],[0,1]], 'S':[[1,0],[-1,0],[0,1],[0,-1]], 'PAIN':[[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]}
extend = {
    "L": [[0, 1, 0], [0, 1, 1], [0, 0, 0]],
    "J": [[0, 1, 0], [1, 1, 0], [0, 0, 0]],
    "7": [[0, 0, 0], [1, 1, 0], [0, 1, 0]],
    "F": [[0, 0, 0], [0, 1, 1], [0, 1, 0]],
    "|": [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
    "-": [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
    "S": [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
    ".": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
}

def part1(data):
    G = nx.DiGraph()

    for y in range(len(data)):
        for x in range(len(data[0])):
            nodeid = y * len(data[0]) + x
            if data[y][x] == "S":
                start = nodeid
            elif data[y][x] != ".":
                edges = []
                for d in directions[data[y][x]]:
                    if d[0] + y >= 0 and d[0] + y < len(data):
                        if d[1] + x >= 0 and d[1] + x < len(data[0]):
                            edges.append((nodeid, d[0] * len(data[0]) + nodeid + d[1]))
                G.add_edges_from(edges)

    neighbors = list(G.in_edges(start))
    G.add_edge(start, neighbors[0][0])
    path = nx.shortest_path(G, start, neighbors[1][0])
    return path, len(path) // 2


def part2(data, path):
    total = 0
    void = []
    for y in range(len(data)):
        voids = []
        for x in range(len(data[0])):
            if y * len(data[0]) + x in path: voids.append(data[y][x])
            else: voids.append('.')
        void.append(voids)
    for y in range(len(data)):
        void[y].insert(0, '.')
        void[y].append('.')
    void.insert(0, ['.' for x in range(len(data[0]) + 2)])
    void.append(['.' for x in range(len(data[0]) + 2)])

    extended = np.zeros((len(void) * 3, len(void[0]) * 3), dtype=int)
    for y in range(len(void)):
        for x in range(len(void[0])):
            extended[y * 3 : y * 3 + 3, x * 3 : x * 3 + 3] = extend[void[y][x]]

    for y in range(len(void)):
        for x in range(len(void[0])):
            extended[y * 3 : y * 3 + 3][x * 3 : x * 3 + 3] = extend[void[y][x]]

    fill = flood_fill(extended, (0, 0), 1)
    res = 0
    for y in range(len(void)):
        for x in range(len(void[0])):
            check = fill[y * 3 : y * 3 + 3, x * 3 : x * 3 + 3]
            if not check.any():
                res += 1
    print(res)

    for x in void:
        print("".join(x))

    for y in range(len(void)):
        for x in range(len(void[0])):
            check = extended[y * 3 : y * 3 + 3][x * 3 : x * 3 + 3]
            if not check.any():
                total += 1

    return total


path, total = part1(data)
print(total)
print(part2(data, path))