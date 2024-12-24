from collections import defaultdict

def part1(nums):
    total = 0
    seq_dict = defaultdict(int)

    for num in nums:
        seen = set()
        seq = [0]*4
        prev_price = num % 10

        for i in range(2000):
            new = num * 64
            num = num ^ new % 16777216

            new = num // 32
            num = num ^ new % 16777216

            new = num * 2048
            num = num ^ new % 16777216

            price = num % 10
            seq = seq[1:] + [price - prev_price]
            prev_price = price

            temp = tuple(seq)
            if i >= 3 and temp not in seen:
                seen.add(temp)
                seq_dict[temp] += prev_price
        total += num
    return total, max(seq_dict.values())

nums = [int(x) for x in open('data/day22.txt').readlines()]
print(part1(nums))
