lines = open("day8.txt").readlines()
total = 0

for i in range(len(lines)):
    for j in range(len(lines)):
        scenic = 1
        for k in range(4):
            if k == 0:
                visable = 0
                for x in range(j - 1, -1, -1):
                    if int(lines[i][x]) < int(lines[i][j]):
                        visable += 1
                    else:
                        visable +=1
                        break
                # print(i,j,visable)
                scenic *= visable
            if k == 1:
                visable = 0
                for x in range(j + 1, len(lines), 1):
                    if int(lines[i][x]) < int(lines[i][j]):
                        visable += 1
                    else:
                        visable +=1
                        break
                # print(i,j,visable)
                scenic *= visable
            if k == 2:
                visable = 0
                for x in range(i - 1, -1, -1):
                    if int(lines[x][j]) < int(lines[i][j]):
                        visable += 1
                    else:
                        visable +=1
                        break
                # print(i,j,visable)
                scenic *= visable
            if k == 3:
                visable = 0
                for x in range(i + 1, len(lines), 1):
                    if int(lines[x][j]) < int(lines[i][j]):
                        visable += 1
                    else:
                        visable +=1
                        break
                # print(i,j,visable)
                scenic *= visable
        if scenic > total:
            # print(i,j,lines[i][j],scenic)
            total = scenic

print(total)