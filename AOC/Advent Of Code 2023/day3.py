data = open("day3.txt").readlines()
ranges = [0, 1]

def getnumbers(data):
    allnums = []
    for i in range(len(data)):
        x = list(data[i].strip())
        num = ['', (0, 0), (0,0), 0]
        for j in range(len(x)):
            if x[j].isnumeric():
                if num[0] == '': num[1] = (i, j)
                num[0] += x[j]
            else:
                if num[0] != '':
                    num[0] = int(num[0])
                    num[2] = (i,j - 1)
                    allnums.append(num)
                    num = ['', (0, 0), (0,0), 0]
        if num[0] != '':
            num[0] = int(num[0])
            num[2] = (i,j - 1)
            allnums.append(num)
    return allnums

def getsymbols(data):
    allsymbols = []
    for i in range(len(data)):
        x = list(data[i].strip())
        for j in range(len(x)):
            if not x[j].isnumeric() and x[j] != '.':
                allsymbols.append((i, j))
    return allsymbols



def part1(data):
    total = 0
    nums = getnumbers(data)
    symbols = getsymbols(data)

    for ys, xs in symbols:
        for num in nums:
            if abs(ys - num[1][0]) in ranges:
                if abs(xs - num[1][1]) in ranges or abs(xs - num[2][1]) in ranges:
                    if num[3] == 0:
                        total += num[0]
                        num[3] = 1
    return total

def part2(data):
    total = 0
    nums = getnumbers(data)
    symbols = getsymbols(data)

    for ys, xs in symbols:
        nodes = []
        for num in nums:
            if abs(ys - num[1][0]) in ranges:
                if abs(xs - num[1][1]) in ranges or abs(xs - num[2][1]) in ranges:
                    nodes.append(num[0])
        if len(nodes) == 2:
            total += nodes[0] * nodes[1]
    return total


print(part1(data))
print(part2(data))