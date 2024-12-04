lines = open("day8.txt").readlines()
check = open("day8.txt").readlines()
total = 0
line = 0
line2 = 0
jump = []

for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")
    lines[i] = lines[i].split()
    check[i] = 0
    if lines[i][0] == "jmp" or lines[i][0] == "nop":
        jump.append([lines[i][0], i])


while line < len(lines):
    line = 0
    total = 0
    if jump[line2][0] == "jmp":
        lines[jump[line2][1]][0] = "nop"
    else:
        lines[jump[line2][1]][0] = "jmp"
    while check[line] != 1:
        match lines[line][0]:
            case "acc":
                check[line] = 1
                total += int(lines[line][1])
                line += 1
            case "jmp":
                check[line] = 1
                line += int(lines[line][1])
            case "nop":
                check[line] = 1
                line += 1
        if line < len(lines):
            print(total)
    for i in range(len(check)):
        check[i] = 0
    lines[jump[line2][1]][0] = jump[line2][0]
    line2 += 1

print(total)