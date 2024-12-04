import time

lines = open("day5.txt").readlines()
data = []
start = time.time()

for i in range(len(lines)):
    lines[i] = lines[i].replace("F", "0")
    lines[i] = lines[i].replace("B", "1")
    lines[i] = lines[i].replace("L", "0")
    lines[i] = lines[i].replace("R", "1")

    row = int(lines[i][0]+lines[i][1]+lines[i][2]+lines[i][3]+lines[i][4]+lines[i][5]+lines[i][6], 2)
    column = int(lines[i][7]+lines[i][8]+lines[i][9], 2)
    ID = row * 8 + column

    data.append(ID)

data.sort()

for i in range(len(data)):
    if data[i+1] - data[i] != 1:
        print(data[i]+1)
        print(time.time()-start)