lines = open("day4.txt").readlines()
data = []
total = 0

for x in lines:
    x = x.strip().split(",")
    x = [x[0].split("-"), x[1].split("-")]
    if int(x[0][0]) <= int(x[1][0]) and int(x[0][1]) >= int(x[1][1]):
        total += 1
        continue
    elif int(x[0][0]) >= int(x[1][0]) and int(x[0][1]) <= int(x[1][1]):
        total += 1
        continue
    else:
        print(x)
print(total)
