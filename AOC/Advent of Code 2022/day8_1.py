lines = open("day8.txt").readlines()
total = 0

for i in range(len(lines)):
    if i == 0 or i == len(lines) - 1:
        # print(i)
        total += len(lines)
        # print(total)
        continue
    else:
        for j in range(len(lines)):
            if j == 0 or j == len(lines) - 1:
                # print(i,j)
                total += 1
                # print(total)
            else:
                # print(i,j,int(lines[i][j]), max(int(lines[i][x]) for x in range(j)), max(int(lines[i][x]) for x in range(j, len(lines[i]) - 1, 1)),  max(int(lines[x][j]) for x in range(i)), max(int(lines[x][j]) for x in range(i, len(lines), 1)))
                if max(int(lines[i][x]) for x in range(j)) < int(lines[i][j]) or max(int(lines[i][x]) for x in range(j + 1, len(lines), 1)) < int(lines[i][j]) or max(int(lines[x][j]) for x in range(i)) < int(lines[i][j]) or max(int(lines[x][j]) for x in range(i + 1, len(lines), 1)) < int(lines[i][j]):
                    total += 1
                    # print(total)

print(total)