import queue

def part1(equations, part2=False):
    total = 0
    for eq in equations:
        eq = eq.split()
        result = int(eq[0][:-1])
        nums = [int(x) for x in eq[1:]]

        q = queue.Queue()
        q.put((result, len(nums) - 1))

        while not q.empty():
            current, index = q.get()

            if index == 0:
                if current == nums[0]:
                    total += result
                    break
                continue

            if current % nums[index] == 0:
                q.put((current // nums[index], index - 1))

            q.put((current - nums[index], index - 1))

            if part2:
                str_current = str(current)
                str_num = str(nums[index])
                if str_current.endswith(str_num):
                    prefix = str_current[:-len(str_num)]
                    if prefix.isdigit():
                        q.put((int(prefix), index - 1))
    return total


equations = open("data/day7.txt").readlines()

print(part1(equations))
print(part1(equations, True))