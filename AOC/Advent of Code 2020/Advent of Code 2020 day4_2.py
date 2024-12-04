import time

lines = open("day4.txt").readlines()
total = 0
scanner = 0
data = []
eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

start = time.time()

for i in range(len(lines)):
    if lines[i] != "\n":
        lines[i] = lines[i].strip('\n')
        lines[i] = lines[i].replace(":", " ")

for i in range(len(lines)):
    if lines[i] != "\n":
        data = lines[i].split()

        for j in range(len(data)):
            if data[j].find("byr") != -1 and int(data[j+1]) >= 1920 and int(data[j+1]) <= 2002:
                scanner += 1
            if data[j].find("iyr") != -1 and int(data[j+1]) >= 2010 and int(data[j+1]) <= 2020:
                scanner += 1
            if data[j].find("eyr") != -1 and int(data[j+1]) >= 2020 and int(data[j+1]) <= 2030:
                scanner += 1
            if data[j].find("hgt") != -1:
                if data[j+1].find("cm") != -1:
                    data[j+1] = data[j+1].strip("cm")
                    if int(data[j+1]) >= 150 and int(data[j+1]) <= 193:
                        scanner += 1
                if data[j+1].find("in") != -1:
                    data[j+1] = data[j+1].strip("in")
                    if int(data[j+1]) >= 59 and int(data[j+1]) <= 76:
                        scanner += 1
            if data[j].find("hcl") != -1 and data[j+1][0] == "#" and len(data[j+1]) == 7:
                scanner += 1
            if data[j].find("ecl") != -1:
                for x in range(len(eyes)):
                    if data[j+1] == eyes[x]:
                        scanner += 1
            if data[j].find("pid") != -1 and len(data[j+1]) == 9:
                scanner += 1
    if lines[i] == "\n":
        if scanner == 7:
            total += 1
        scanner = 0

print(total)
print(time.time()-start)