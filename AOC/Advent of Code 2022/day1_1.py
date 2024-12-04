# lines = open("day1.txt").readlines()
# data = []
# t = 0

# for i in range(len(lines)):
#     lines[i] = lines[i].strip('\n')
#     if lines[i] != '':
#         t += int(lines[i])
#     else:
#         data.append(t)
#         t = 0

# data.sort(reverse=True)
# print(data[0]+data[1]+data[2])

# lines = open("day1.txt").read(). split("\n\n")
# totals = sorted([sum([int(x) for x in l.split("\n") if x]) for l in lines])
# print(totals[-1] )
# print(sum(totals[-3:]))

# data = {"test":[["a"],[1]]}
# data["test"][0].append("b")
# print(data["test"][0])

# test = "abcdef"
# print(test[:0])

for x in range(9-1,-1,-1):
    print(x)