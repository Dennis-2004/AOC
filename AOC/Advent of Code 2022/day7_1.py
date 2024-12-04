lines = open("day7.txt").readlines()
data = {}
dir = ""
store = []
total = 0

for x in lines:
    x = x.split()
    if len(x) == 3 and x[0] == "$" and x[1] == "cd":
        if x[2] == "/" or dir == "/":
            dir = dir + x[2]
        elif x[2] == "..":
            temp = dir.split("/")
            dir = ""
            for y in range(len(temp) - 1):
                if dir == "/":
                    dir = dir + temp[y]
                else:
                    dir = dir + "/" + temp[y]
        else:
            dir = dir + "/" + x[2]
    elif x[0] == "dir":
        temp_dir = dir
        if temp_dir == "/":
            temp_dir = temp_dir + x[1]
        else:
            temp_dir = temp_dir + "/" + x[1]
        if dir in data:
            data[dir][0].append(temp_dir)
        else:
            data[dir] = [[temp_dir], 0]
    elif x[0].isnumeric():
        if dir in data:
            data[dir][1] += int(x[0])
        else:
            data[dir] = [[], int(x[0])]


def recursive(x):
    # print(data[x])
    # print(x, data[x][0],data[x][1])
    if len(data[x][0]) == 0:
        return data[x][1]
    else:
        for y in data[x][0]:
            # print(type(data[x][1]))
            # print(y)
            data[x][1] += recursive(y)
            # print(x, data[x][0],data[x][1], y)
        return data[x][1]

recursive("/")

for x in data:
    if data[x][1] <= 100000:
        total += data[x][1]

available = 70000000 - data["/"][1]
needed = 30000000 - available

best = data["/"][1]

for x in data:
    if data[x][1] > needed and data[x][1] < best:
        best = data[x][1]

print(best)
print(total)