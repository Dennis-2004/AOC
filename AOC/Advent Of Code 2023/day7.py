data = open("day7.txt").readlines()

for i, x in enumerate(data):
    data[i] = (x.strip().split()[0], int(x.strip().split()[1]))


def getType(hand, joker):
    if joker: cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
    else: cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    J = 0
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in hand:
        count[cards.index(x)] += 1
    if joker:
        J = count[0]
        count[0] = 0
    count.sort(reverse=True)
    count[0] += J

    if count[0] == 5: return 6
    elif count[0] == 4: return 5
    elif count[0] == 3:
        if count[1] == 2: return 4
        else: return 3
    elif count[0] == 2:
        if count[1] == 2: return 2
        else: return 1
    else: return 0

def compareHand(hand1, hand2, joker):
    if joker: cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
    else: cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    type1 = getType(hand1[0], joker)
    type2 = getType(hand2[0], joker)

    if type1 > type2: return 0
    elif type1 < type2: return 1
    else:
        for i in range(len(hand1[0])):
            if cards.index(hand1[0][i]) > cards.index(hand2[0][i]): return 0
            elif cards.index(hand1[0][i]) < cards.index(hand2[0][i]): return 1


def sort(data, joker=False):
    total = 0
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and compareHand(key, data[j], joker):
            data[j + 1] = data[j]
            j = j - 1

        data[j + 1] = key

    for i, x in enumerate(data):
        total += x[1] * (i + 1)

    return total

def part1(data):
    return sort(data)

def part2(data):
    return sort(data, True)

# print(part1(data))
print(part2(data))
