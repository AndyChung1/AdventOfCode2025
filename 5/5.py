from pathlib import Path

input_file = Path(__file__).parent / "input.txt"


def part_1():
    ranges = []
    res = 0
    with open(input_file) as file:
        for line in file:
            if line == '\n':
                break
            input = line.rstrip().split('-')
            ranges.append((int(input[0]), int(input[1])))
        
        for id in file:
            for low, high in ranges:
                if low <= int(id) <= high:
                    res += 1
                    break

    return res

print(part_1())


def is_overlap(min1, max1, min2, max2):
    if max1 < min2 or min1 > max2:
        return False

    return True


def add_range_to_unique_ranges(curr_range, unique_ranges):
    curr_low, curr_high = curr_range[0], curr_range[1]
    for ran in unique_ranges:
        if is_overlap(curr_low, curr_high, ran[0], ran[1]):
            ran[0] = min(ran[0], curr_low)
            ran[1] = max(ran[1], curr_high)
            return True

    return False


def part_2():
    unique_ranges = []
    ranges = []
    with open(input_file) as file:
        for line in file:
            if line == '\n':
                break
            input = line.rstrip().split('-')
            input = [int(input[0]), int(input[1])]
            ranges.append(input)

    for input in sorted(ranges):
        if not add_range_to_unique_ranges(input, unique_ranges):
            unique_ranges.append(input)

    res = 0
    for low, high in unique_ranges:
        res += high - low + 1

    return res

print(part_2())
