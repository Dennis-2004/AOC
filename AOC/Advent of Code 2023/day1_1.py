lines = open("day1.txt").readlines()
total = 0

for x in lines:
    x = [s for s in x if s.isdigit()]
    x = x[0] + x[-1]
    total += int(x)

print(total)