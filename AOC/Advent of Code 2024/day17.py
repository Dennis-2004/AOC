class computer:
    def __init__(self, data, a=None, once=False):
        A = a if a else int(data[0].split()[-1])
        B = int(data[1].split()[-1])
        C = int(data[2].split()[-1])
        self.combo = [0, 1, 2, 3, A, B, C]
        self.P = [int(x) for x in data[4].split()[-1].split(',')]
        self.pos = 0
        self.increment = True
        self.once = once


    def instruction(self, op, co):
        output = None

        match op:
            case 0:
                self.combo[4] = self.combo[4] // (2**self.combo[co])
            case 1:
                self.combo[5] = self.combo[5] ^ co
            case 2:
                self.combo[5] = self.combo[co] % 8
            case 3:
                if self.once:
                    self.pos = 99999
                elif self.combo[4]:
                    self.pos = co
                    self.increment = False
            case 4:
                self.combo[5] = self.combo[5] ^ self.combo[6]
            case 5:
                output = self.combo[co] % 8
            case 6:
                self.combo[5] = self.combo[4] // (2**self.combo[co])
            case 7:
                self.combo[6] = self.combo[4] // (2**self.combo[co])

        return output

    def run(self):
        n = len(self.P)
        res = ''
        while self.pos < n:
            output = self.instruction(self.P[self.pos], self.P[self.pos + 1])

            if output is not None:
                res += f'{output},'
            if self.increment:
                self.pos += 2
            self.increment = True
        return res[:-1]


def part2(instructions, data, a, results, level):
    val = instructions[-level]

    for i in range(8):
        test = int(computer(data, a+i, True).run())

        if test == val:
            if level == len(instructions):
                results.append(a+i)
            elif level < len(instructions):
                part2(instructions, data, (a+i)*8, results, level+1)


data = open('data/day17.txt').readlines()
comp = computer(data)
print(comp.run())

results = []
part2(comp.P, data, 0, results, 1)
print(min(results))