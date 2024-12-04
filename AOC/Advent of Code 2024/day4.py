import re

def part1(hor):
    ver = hor.split('\n')
    dia1 = hor.split('\n')
    dia2 = hor.split('\n')

    ver = "\n".join(["".join([row[i] for row in ver]) for i in range(len(ver[0]))])

    temp1 = []
    temp2 = []
    for y in range(len(dia1) * 2 - 1):
        temp1.append(''.join([dia1[y - i][i] for i in range(y + 1) if (0 <= y - i < len(dia1) and 0 <= i < len(dia1[0]))]))
        temp2.append(''.join([dia2[y - i][len(dia2[0]) - i - 1] for i in range(y + 1) if (0 <= y - i < len(dia2) and 0 <= i < len(dia2[0]))]))
    dia1 = "\n".join(temp1)
    dia2 = "\n".join(temp2)

    query = r'(?=(XMAS|SAMX))'

    total = len(re.findall(query, hor))
    total += len(re.findall(query, ver))
    total += len(re.findall(query, dia1))
    total += len(re.findall(query, dia2))

    return total


def part2(data):
    data = data.split('\n')
    total = 0
    patterns = ["MMASS", "SMASM", "SSAMM", "MSAMS"]
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            temp = ""
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if abs(i*j) == 1 or (i == 0 and j == 0):
                        temp += data[y + i][x + j]
            if temp in patterns:
                total += 1
    return total

lines = open("day4.txt").read()

print(part2(lines))

