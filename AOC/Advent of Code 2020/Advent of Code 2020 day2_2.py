from ast import For

lines = open("day2.txt").readlines()
data = []
total = 0

for i in range(len(lines)):
    lines[i] = lines[i].replace("-"," ")
    lines[i] = lines[i].replace(":","")
    data.append(lines[i].split())

for i in range(len(lines)):
    password = [letter for letter in data[i][3]]
    pos1 = int(data[i][0])
    pos2 = int(data[i][1])

    if (password[pos1 - 1] == data[i][2] or password[pos2 - 1] == data[i][2]) and not (password[pos1 - 1] == data[i][2] and password[pos2 - 1] == data[i][2]):
        total += 1

print(total)