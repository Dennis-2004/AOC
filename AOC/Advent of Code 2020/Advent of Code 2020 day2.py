from ast import For

lines = open("day2.txt").readlines()
data = []
total = 0

for i in range(len(lines)):
    lines[i] = lines[i].replace("-"," ")
    lines[i] = lines[i].replace(":","")
    data.append(lines[i].split())

for i in range(len(lines)):
    password = [letter for letter in data[i][3]]
    min = int(data[i][0])
    max = int(data[i][1])
    temp = 0
    
    for j in range(len(password)):
        if data[i][2] == password[j]:
            temp += 1
    
    if temp >= min and temp<= max:
        total += 1

print(total)