from pathlib import Path
from functools import cache

input_file = Path(__file__).parent / "input.txt"

adj_list = {}
with open(input_file) as file:
    for line in file:
        device, outputs = line.split(':')
        outputs = outputs.strip().split()
        adj_list[device] = outputs


res = 0
def dfs(device, visited):
    global res
    if device in visited:
        return
    if device == "out":
        res += 1
        return
    visited.add(device)
    for output in adj_list[device]:
        dfs(output, visited)
        if output != 'out':
            visited.remove(output)

dfs('you', set())
print(res)


@cache
def dfs_2(device, fft, dac):
    res = 0
    if device == "out":
        return 1 if fft and dac else 0
    
    if device == 'dac':
        dac = True
    elif device == 'fft':
        fft = True
    for output in adj_list[device]:
        res += dfs_2(output, fft, dac)
        
    return res


print(dfs_2('svr', False, False))
