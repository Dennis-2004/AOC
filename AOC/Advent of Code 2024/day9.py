import bisect

def part1(disk):
    head = 0
    tail = len(disk) - 1

    while 1:
        if disk[tail] >= 0:
            while disk[head] >= 0 and head < tail:
                head += 1
            if head == tail:
                break
            disk[head] = disk[tail]
            disk[tail] = -1
        tail -= 1
    total = sum([x*i if x != -1 else 0 for i, x in enumerate(disk)])
    return total


def part2(files, empty):
    i = len(files) - 1
    while i >= 0:
        for y in empty:
            if files[i][1] <= y[1] and files[i][0] > y[0]:
                temp = files[i][1]
                length = y[1] - temp
                bisect.insort(empty, files[i][:-1])
                files[i][0] = y[0]
                bisect.insort(files, files.pop(i))
                if length:
                    y[0] += temp
                    y[1] -= temp
                else:
                    empty.remove(y)
                i += 1
                break
        i -= 1
    return sum(sum([[x[2]*i for i in range(x[0], x[0]+x[1])] for x in files],[]))


disk = open("day9.txt").readline().split()
disk = [int(x) for x in disk[0]]

files = []
empty = []
index = 0

for i, x in enumerate(disk):
    if i%2==0:
        files.append([index, x, int(i/2)])
    else:
        if x > 0:
            empty.append([index, x])
    index += x

disk = sum([[int(i/2)]*x if i%2==0 else [-1]*x for i, x in enumerate(disk)], [])

print(part2(files, empty))