from math import log10
from collections import defaultdict

def parts(stones, n):
    stone_dict = defaultdict(int)
    for stone in stones:
        stone_dict[stone] += 1

    for i in range(n):
        blinked = defaultdict(int)
        for stone in stone_dict.keys():
            if stone == 0:
                blinked[1] += stone_dict[stone]
            elif (int(log10(stone)) + 1) % 2 == 0:
                pow = (10**((int(log10(stone)) + 1)/2))
                first_half = int(stone/pow)
                second_half = int(stone - first_half * pow)
                blinked[first_half] += stone_dict[stone]
                blinked[second_half] += stone_dict[stone]
            else:
                blinked[stone*2024] += stone_dict[stone]
        stone_dict = blinked
    return sum(stone_dict.values())


stones = [int(x) for x in open("day11.txt").readlines()[0].split()]
print(parts(stones, 75))