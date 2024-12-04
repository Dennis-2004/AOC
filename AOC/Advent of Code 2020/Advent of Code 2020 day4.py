import time
lines = open("day4.txt").readlines()
total = 0
scanner = 0
data = []
cred = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
start = time.time()

for i in range(len(lines)):
    if lines[i] != "\n":
        for j in range(len(cred)):
            if lines[i].find(cred[j]) != -1:
                scanner += 1
    if lines[i] == "\n":
        if scanner == 7:
            total += 1
        scanner = 0

print(total)
print(time.time()-start)