def part1(design, patterns, memo):
    if design in memo:
        return memo[design]
    if design == "":
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            if part1(design[len(pattern):], patterns, memo):
                memo[design] = True
                return True

    memo[design] = False
    return False


def part2(design, patterns, memo):
    if design in memo:
        return memo[design]
    if design == "":
        return 1

    total_ways = 0
    for pattern in patterns:
        if design.startswith(pattern):
            total_ways += part2(design[len(pattern):], patterns, memo)

    memo[design] = total_ways
    return total_ways


def get_answer(patterns, designs):
    memo1 = {}
    memo2 = {}
    count = 0
    total = 0

    for design in designs:
        if part1(design, patterns, memo1):
            count += 1
        total += part2(design, patterns, memo2)

    return count, total


data = open('data/day19.txt').readlines()
patterns = [x.strip() for x in data[0].strip().split(',')]
designs = [x.strip() for x in data[2:]]

print(get_answer(patterns, designs))