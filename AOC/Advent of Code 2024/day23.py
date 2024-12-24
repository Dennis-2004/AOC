from collections import defaultdict
import time

def part1(data):
    triangles = set()

    for node in data:
        for neighbor in data[node]:
            for mutual_neighbor in data[neighbor]:
                if mutual_neighbor != node and mutual_neighbor in data[node]:
                    triangle = tuple(sorted([node, neighbor, mutual_neighbor]))
                    triangles.add(triangle)

    triangles_with_t = [
        triangle for triangle in triangles
        if any(computer.startswith('t') for computer in triangle)
    ]

    return len(triangles_with_t)


def part2(data):
    def bron_kerbosch(R, P, X, cliques):
        if not P and not X:
            cliques.append(R)
            return
        for node in list(P):
            bron_kerbosch(R | {node}, P & data[node], X & data[node], cliques)
            P.remove(node)
            X.add(node)

    nodes = set(data.keys())
    cliques = []
    bron_kerbosch(set(), nodes, set(), cliques)

    largest = list(max(cliques, key=len))
    return ','.join(sorted(largest))


LAN = defaultdict(set)
for line in open('data/day23.txt').readlines():
    a, b = line.strip().split("-")
    LAN[a].add(b)
    LAN[b].add(a)

print(part1(LAN))
print(part2(LAN))