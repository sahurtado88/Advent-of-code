import sys


with open(sys.argv[1], "r") as f:
    inputs = f.read().split('\n\n')

items = {"#": [], ".": []}
for grid_str in inputs:
    grid = list(zip(*grid_str.split('\n')))
    items[grid[0][0]].append([len([c for c in r if c == "#"]) for r in grid])

part1 = 0
for lock in items["#"]:
    for key in items["."]:
        if all(l + k <= 7 for l, k in zip(lock, key)):
            part1 += 1

print(f'Part 1: {part1}')
