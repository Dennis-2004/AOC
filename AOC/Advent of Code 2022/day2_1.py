lines = open("day2.txt").readlines()
total = 0

for i in lines:
    if i[0] == 'A':
        if i[2] == 'X':
            total += 4
        elif i[2] == 'Y':
            total += 8
        elif i[2] == 'Z':
            total += 3
    elif i[0] == 'B':
        if i[2] == 'X':
            total += 1
        elif i[2] == 'Y':
            total += 5
        elif i[2] == 'Z':
            total += 9
    elif i[0] == 'C':
        if i[2] == 'X':
            total += 7
        elif i[2] == 'Y':
            total += 2
        elif i[2] == 'Z':
            total += 6

print(total)