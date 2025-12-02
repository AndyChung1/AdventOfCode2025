def main():
    res, curr = 0, 50
    with open('input.txt') as file:
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

print(main())


# SUBTRACTION case:
# if rotation > curr: do curr - curr, 100 - remainder
# remainder = rotation - curr

# ADDITION CASE:
# if rotation > 99 - curr: do curr + (99 - curr), remainder + 1
# remainder = rotation - (99 - curr)
