
lines = open("day3.txt").readlines()
total = 0
x = 0
y = 0
test = []

while y < len(lines):
    test.append(lines[y][x])
    if lines[y][x] == "#":
        total += 1
    
    x += 1
    y += 2

    if x > len(lines[0]) - 2:
        x = x - (len(lines[0]) - 1)

print(total)