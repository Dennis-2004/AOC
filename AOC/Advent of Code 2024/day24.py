import re

def get_value(wire, operations, inputs):
    if wire in inputs:
        return inputs[wire]
    else:
        oper = operations[wire]
        val = gates[oper[1]](get_value(oper[0], operations, inputs), get_value(oper[2], operations, inputs))
        inputs[wire] = val
        return val

def part1(operations, inputs):
    ends = sorted([s for s in list(operations.keys()) if re.fullmatch(r'z\d\d', s)])
    ends = [get_value(x, operations, inputs) for x in ends]
    return int(''.join(map(str, ends[::-1])),2)


def part2(operations, inputs):
    ans = []
    gates_op = operations.items()
    faultz = []
    faulto = []

    for out, op in gates_op:
        if re.fullmatch(r'z\d\d', out):
            if op[1] != 'XOR':
                if out != 'z45':
                    faultz.append(out)
        elif not (re.fullmatch(r'x\d\d', op[0]) or re.fullmatch(r'y\d\d', op[0])):
            if op[1] == 'XOR':
                faulto.append(out)
    ans += faulto
    ans += faultz
    for fault in faulto:
        stack = [fault]
        while stack:
            elem = stack.pop()
            for out, op in gates_op:
                if elem in op:
                    if re.fullmatch(r'z\d\d', out):
                        stack = []
                        temp = operations[fault]
                        operations[fault] = operations['z'+str(int(out[1:])-1)]
                        operations['z'+str(int(out[1:])-1)] = temp
                        break
                    stack.append(out)

    for i in range(45):
        inputs = {}
        new = operations.copy()
        xbin = ''
        ybin = ''
        for x in data[0].split('\n'):
            x = x.split(':')
            inputs[x[0]] = int(x[1].strip())
            if x[0].startswith('x'):
                xbin += x[1].strip()
            else:
                ybin += x[1].strip()
        if i < 10:
            val = 'x0' + str(i)
        else:
            val = 'x' + str(i)
        gates_op = new.items()
        temp1 = None
        temp2 = None
        for out, op in gates_op:
            if val in op:
                if temp1:
                    temp2 = out
                    break
                temp1 = out
        temp = new[temp1]
        new[temp1] = new[temp2]
        new[temp2] = temp

        real = int(''.join(map(str, xbin[::-1])),2) + int(''.join(map(str, ybin[::-1])),2)
        mine = part1(new, inputs)
        if real == mine:
            ans += [temp1, temp2]
    return ','.join(sorted(ans))


data = open('data/day24.txt').read()
data = data.split('\n\n')
inputs = {}
operations = {}
gates = {'AND': lambda x, y: x & y,
         'OR': lambda x, y: x | y,
         'XOR': lambda x, y: x ^ y}

for x in data[0].split('\n'):
    x = x.split(':')
    inputs[x[0]] = int(x[1].strip())

for x in data[1].split('\n'):
    x = x.split()
    operations[x[-1]] = x[:3]

print(part1(operations, inputs))
print(part2(operations, inputs))