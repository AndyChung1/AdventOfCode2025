from pathlib import Path
import math

input_file = Path(__file__).parent / "input.txt"

def part_1():
    lines = []
    with open(input_file) as file:
        for line in file:
            line = line.rstrip().split(' ')
            line = [l for l in line if l != '']
            lines.append(line)
    
    cols = [list(col) for col in zip(*lines)]
    res = 0
    for col in cols:
        operator = col.pop()
        col = map(int, col)
        if operator == '+':
            res += sum(col)
        else:
            res += math.prod(col)
    
    return res

print(part_1())


def part_2():
    lines = []
    with open(input_file) as file:
        for line in file:
            line = line.rstrip('\n')
            lines.append(line)

    cols = [list(col) for col in zip(*lines)]
    res  = 0
    curr = []
    for col in cols:
        if col[-1] == '*' or col[-1] == '+':
            operator = col.pop()

        if all(s == ' ' for s in col):
            if operator == '+':
                res += sum(curr)
            else:
                res += math.prod(curr)
            curr = []
            continue
        
        curr.append(int(''.join(col)))

    if operator == '+':
        res += sum(curr)
    else:
        res += math.prod(curr)

    return res

print(part_2())