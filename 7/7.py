from pathlib import Path

input_file = Path(__file__).parent / "input.txt"


lines = []
with open(input_file) as file:
    for line in file:
        lines.append(line.rstrip())


def is_in_bounds(row, col):
    return 0 <= row < len(lines) and 0 <= col < len(lines[0])


def part_1():
    beams = {lines[0].index('S')}
    res = 0
    for line in lines:
        beams_to_replace = []
        for beam in beams:
            if line[beam] == '^':
                res += 1
                beams_to_replace.append(beam)

        for beam in beams_to_replace:
            beams.remove(beam)
            beams.add(beam - 1)
            beams.add(beam + 1)

    return res

print(part_1())


# part 2

cache = {}
def dfs(row, col):
    if (row, col) in cache:
        return cache[(row, col)]

    if not (
        0 <= row < len(lines)
        and 0 <= col < len(lines[0])
    ):
        cache[(row, col)] = 1
        return 1
    
    if lines[row][col] == '^':
        res = dfs(row, col - 1) + dfs(row, col + 1)
    
    else:
        res = dfs(row + 1, col)

    cache[(row, col)] = res
    return res


print(dfs(0, lines[0].index('S')))
