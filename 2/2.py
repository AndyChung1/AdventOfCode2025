from pathlib import Path

def remove_dash(s):
    s = s.split('-')
    return (int(s[0]), int(s[1]))

input_file = Path(__file__).parent / "input.txt"
input = input_file.read_text()
split_input = input.split(',')

# PART 1

def is_invalid(id: int):
    id_str = str(id)
    return id_str[:len(id_str) // 2] == id_str[len(id_str) // 2:]


def get_invalid_ids_in_range(low, high):
    res = []
    for num in range(low, high + 1):
        if is_invalid(num):
            res.append(num)
    return res


def part_1():
    ranges = map(remove_dash, split_input)
    res = []
    for low, high in ranges:
        res.extend(get_invalid_ids_in_range(low, high))
    
    return sum(res)


# PART 2

def is_invalid_2(id: int):
    id_str = str(id)
    n = len(id_str)

    for i in range(1, n // 2 + 1):
        substring = id_str[:i]
        if n % i == 0:
            if substring * (n // i) == id_str:
                return True
    return False


def get_invalid_ids_in_range_2(low, high):
    res = []
    for num in range(low, high + 1):
        if is_invalid_2(num):
            res.append(num)

    return res


def part_2():
    ranges = map(remove_dash, split_input)
    res = []
    for low, high in ranges:
        res.extend(get_invalid_ids_in_range_2(low, high))

    return sum(res)


print(part_1())
print(part_2())