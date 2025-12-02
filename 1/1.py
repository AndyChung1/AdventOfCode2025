from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

def part_1():
    res, curr = 0, 50
    with open(input_path) as file:
        for line in file:
            input = line.rstrip()
            clicks = int(input[1:]) % 100
            if input[0] == 'R':
                if clicks > 99 - curr:
                    curr = clicks - (99 - curr) - 1
                else:
                    curr += clicks
            
            else:
                if clicks > curr:
                    curr = 100 - (clicks - curr)
                else:
                    curr -= clicks
            
            if curr == 0:
                res += 1
    return res


def part_2():
    p2, curr = 0, 50
    with open(input_path) as file:
        for line in file:
            input = line.rstrip()
            clicks = int(input[1:])
            if input[0] == 'R':
                if clicks > 99 - curr:
                    remaining = clicks - (99 - curr)
                    while remaining:
                        if remaining > 100:
                            remaining -= 100
                            p2 += 1
                        else:
                            curr = remaining - 1
                            remaining = 0
                            if curr != 0:
                                p2 += 1
                
                else:
                    curr += clicks
            
            else:
                if clicks > curr:
                    remaining = clicks - curr
                    while remaining:
                        if remaining > 100:
                            remaining -= 100
                            p2 += 1
                        else:
                            if curr != 0:
                                p2 += 1
                            curr = 100 - remaining
                            remaining = 0
                else:
                    curr -= clicks
            
            if curr == 0:
                p2 += 1

    return p2

print(part_1())
print(part_2())
