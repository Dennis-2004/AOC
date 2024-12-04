lines = open("day6.txt").readlines()
answer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
total = 0
count = 0

for i in range(len(lines)):
    if lines[i] != "\n":
        count += 1
        lines[i] = lines[i].strip('\n')
        
        for j in range(len(lines[i])):
            answer[(ord(lines[i][j])) - 97] += 1
    else:
        for j in range(len(answer)):
            if answer[j] == count:
                answer[j] = 1
            else:
                answer[j] = 0
        print(answer)
        print(count)
        total += sum(answer)
        count = 0
        answer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


print(total)