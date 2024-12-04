lines = open("day6.txt").readlines()
alphabet = set("abcdefghijklmnopqrstuvwxyz")
total = 14
for i in range(len(lines[0])):
    if len(alphabet.intersection(lines[0][i] + lines[0][i+1] + lines[0][i+2] + lines[0][i+3] + lines[0][i+4] + lines[0][i+5] + lines[0][i+6] + lines[0][i+7] + lines[0][i+8] + lines[0][i+9] + lines[0][i+10] + lines[0][i+11] + lines[0][i+12] + lines[0][i+13])) == 14:
        break
    total += 1

print(total)