import re
import sys


def solve_puzzle(puzzle: str, offset: int = 0) -> tuple[int]:
    # Button A: X+94, Y+34
    # Button B: X+22, Y+67
    # Prize: X=8400, Y=5400
    a1, a2 = tuple(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    b1, b2 = tuple(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", puzzle)[0]))
    c1, c2 = tuple(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", puzzle)[0]))
    c1 += offset
    c2 += offset

    # https://en.wikipedia.org/wiki/Cramer%27s_rule
    x = ((c1 * b2) - (b1 * c2)) / ((a1 * b2) - (b1 * a2))
    y = ((a1 * c2) - (c1 * a2)) / ((a1 * b2) - (b1 * a2))

    if int(x) == x and int(y) == y:
        return tuple(map(int, (x, y)))
    return (0, 0)


with open(sys.argv[1], "r") as f:
    puzzles = f.read().split("\n\n")

part1 = 0
part2 = 0
for puzzle in puzzles:
    a, b = solve_puzzle(puzzle)
    part1 += a * 3 + b
    a2, b2 = solve_puzzle(puzzle, offset=10000000000000)
    part2 += a2 * 3 + b2

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
