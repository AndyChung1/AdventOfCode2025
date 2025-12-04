from pathlib import Path

input_file = Path(__file__).parent / "input.txt"

def get_input_1():
    lines = []
    with open(input_file) as file:
        for line in file:
            lines.append(line.strip())
    return lines


def get_input_2():
    lines = []
    with open(input_file) as file:
        for line in file:
            lines.append(list(line.strip()))
    return lines


def is_roll(r, c, grid):
    return not (
        not 0 <= r < len(grid)
        or not 0 <= c < len(grid[0])
        or grid[r][c] == '.'
    )


def dfs(r, c, grid):
    if (
        not 0 <= r < len(grid)
        or not 0 <= c < len(grid[0])
        or grid[r][c] == '.'
    ):
        return

    adjacent_rolls = 0
    for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if is_roll(r + dr, c + dc, grid):
            adjacent_rolls += 1

    if adjacent_rolls < 4:
        return True


def part_1():    
    lines = get_input_1()
    res = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if dfs(r, c, lines):
                res += 1

    return res


def part_2():
    def traverse_grid(grid):
        rolls_removed = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if dfs(r, c, grid):
                    rolls_removed += 1
                    grid[r][c] = '.'

        return rolls_removed

    lines = get_input_2()
    total = 0
    while True:
        rolls_removed = traverse_grid(lines)
        total += rolls_removed
        if rolls_removed == 0:
            break

    return total


print(part_1())
print(part_2())
