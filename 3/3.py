from pathlib import Path

input_file = Path(__file__).parent / "input.txt"

def part_1():
    res = []
    with open(input_file) as file:
        for line in file:
            bank = line.strip()
            largest = 0
            max_tens = 0
            l = 0
            while l < len(bank):
                if int(bank[l]) > max_tens:
                    max_tens = int(bank[l])
                    r = l + 1
                    while r < len(bank):
                        curr = int(bank[l] + bank[r])
                        largest = max(largest, curr)
                        r += 1
                l += 1
            res.append(largest)

        return sum(res)

print(part_1())


def find_largest(s: str):
    # possible index of i'th digit is i to len(s) - remaining + 1
    # start from beginning and choose max from index i to len(s) - remaining + 1
    res = []
    remaining = 12
    start = 0
    while remaining:
        max_index = len(s) - remaining + 1
        max_digit = max(s[start: max_index])
        res.append(max_digit)
        index_of_max = s.index(max_digit, start, max_index)
        start = index_of_max + 1
        remaining -= 1

    return int(''.join(res))


def part_2():
    res = []
    with open(input_file) as file:
        for line in file:
            bank = line.strip()
            largest = find_largest(bank)
            res.append(largest)
    return sum(res)

print(part_2())