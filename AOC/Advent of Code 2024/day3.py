import re

def part1(data):
    muls = re.findall(r'mul\(\d+,\d+\)', data)
    total = 0

    for mul in muls:
        mul = mul.split(',')
        total += int(mul[0].split('(')[1]) * int(mul[1].split(')')[0])

    return total


def part2(data):
    instruction = re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', data)
    do = True
    total = 0

    for x in instruction:
        if x == "don't()":
            do = False
        if x == "do()":
            do = True
        else:
            if do:
                x = x.split(',')
                total += int(x[0].split('(')[1]) * int(x[1].split(')')[0])

    return total

data = open("data/day3.txt").read()

print(part2(data))
