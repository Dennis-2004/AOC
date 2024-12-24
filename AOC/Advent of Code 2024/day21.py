from collections import deque
from functools import cache


data = [x.strip() for x in open('data/day21.txt').readlines()]

numpad = {
    "0": [("2", "^"), ("A", ">")],
    "1": [("2", ">"), ("4", "^")],
    "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
    "3": [("2", "<"), ("6", "^"), ("A", "v")],
    "4": [("1", "v"), ("5", ">"), ("7", "^")],
    "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
    "6": [("3", "v"), ("5", "<"), ("9", "^")],
    "7": [("4", "v"), ("8", ">")],
    "8": [("5", "v"), ("7", "<"), ("9", ">")],
    "9": [("6", "v"), ("8", "<")],
    "A": [("0", "<"), ("3", "^")],
}

keypad = {
    "^": [("A", ">"), ("v", "v")],
    "<": [("v", ">")],
    "v": [("<", "<"), ("^", "^"), (">", ">")],
    ">": [("v", "<"), ("A", "^")],
    "A": [("^", "<"), (">", "v")],
}

pads = [numpad, keypad]


def bfs(start, end, map):
    q = deque([(start, [])])
    seen = set(start)
    shortest = None
    res = []
    while q:
        cur, path = q.popleft()
        if cur == end:
            if shortest is None:
                shortest = len(path)
            if len(path) == shortest:
                res.append("".join(path + ["A"]))
            continue
        if shortest and len(path) >= shortest:
            continue
        for next, dir in map[cur]:
            seen.add(next)
            q.append((next, path + [dir]))
    return res


@cache
def dfs(code, level, i=0):
    pad = pads[i]
    res = 0
    code = "A" + code
    for i in range(len(code)-1):
        paths = bfs(code[i], code[i+1], pad)
        if level == 0:
            res += min(map(len, paths))
        else:
            res += min(dfs(path, level - 1, 1) for path in paths)
    return res

print(sum(dfs(code, 2) * int(code[:3]) for code in data))
print(sum(dfs(code, 25) * int(code[:3]) for code in data))