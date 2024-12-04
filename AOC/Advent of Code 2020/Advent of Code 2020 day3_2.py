lines = open("day3.txt").readlines()
total = 0
tree = 0
run = [1,3,5,7,1]
rise = [1,1,1,1,2]
x = 0
y = 0
test = []

for i in run:
    print("a")
    tree = 0
    x = 0
    y = 0
    while y < len(lines):
        test.append(lines[y][x])
        if lines[y][x] == "#":
            tree += 1
        
        x += run[i]
        y += rise[i]

        if x > len(lines[0]) - 2:
            x = x - (len(lines[0]) - 1)
    
    

total = 1

#for i in tree:
#    total = total * tree[i]

print(tree)