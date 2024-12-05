import re

def part2(rules, order):
    total = 0
    for queue in order:
        correct = []
        update = set(queue)
        while update:
            for x in update:
                if len(rules[x]['pre'].intersection(set(update))) == 0:
                    correct.append(x)
                    update.remove(x)
                    break

        total += int(correct[int(len(correct)/2)])
    return total


def part1(rules, order):
    total = 0
    wrong = []
    for queue in order:
        queue = queue.split(',')
        checked = set([])
        success = True
        for x in queue:
            checked.add(x)
            if len(checked.intersection(rules[x]['post'])):
                wrong.append(queue)
                success = False
                break
        if success:
            total += int(queue[int(len(queue)/2)])
    return total, wrong


text = open("day5.txt").read()
rules_t = re.findall(r'\d+\|\d+', text)
order = re.findall(r'\b\d+(?:,\d+)+\b', text)

rules = {}

for rule in rules_t:
    x, y = rule.split('|')
    if x not in rules:
        rules[x] = {'post':set([]), 'pre':set([])}
    if y not in rules:
        rules[y] = {'post':set([]), 'pre':set([])}
    rules[x]['post'].add(y)
    rules[y]['pre'].add(x)

_, wrong = part1(rules, order)
print(part2(rules, wrong))
