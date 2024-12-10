import re
from itertools import chain

lines = open("day1.txt").readlines()
total = 0

def strtoint(s):
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    found_numbers = []

    for word in numbers.keys():
        offset = 0
        while True:
            if word in s[offset:]:
                found_numbers.append((numbers[word], s[offset:].find(word) + offset))
                offset = s[offset:].find(word) + offset + len(word)
            else:
                break

    if found_numbers:
        return [item[0] for item in sorted(found_numbers, key=lambda x: x[1])]
    else:
        return "0"

for x in lines:
    x = re.findall(r'\d+|[a-zA-Z]+', x)
    x = [strtoint(s) if not s.isnumeric() else list(s) for s in x]
    x = flattened_list = list(chain(*x))
    x = [s for s in x if s != "0"]
    x = x[0] + x[-1]
    total += int(x)


print(total)