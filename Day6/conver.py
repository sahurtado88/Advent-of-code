import numpy as np

class Solution:

    Up = 1j
    TurnRight = -1j

    def part_one(self, input):
        map_, start = self.parse(input)
        return len(self.walk(map_, start)[0])

    def part_two(self, input):
        map_, start = self.parse(input)
        positions = self.walk(map_, start)[0]
        loops = 0
        # simply try a blocker in each locations visited by the guard and count the loops
        for block in (pos for pos in positions if map_[pos] == '.'):
            map_[block] = '#'
            if self.walk(map_, start)[1]:
                loops += 1
            map_[block] = '.'
        return loops

    # returns the positions visited when starting from 'pos', isLoop is set if the 
    # guard enters a cycle.
    def walk(self, map_, pos):
        seen = set()
        dir_ = self.Up
        while pos in map_ and (pos, dir_) not in seen:
            seen.add((pos, dir_))
            if map_.get(pos + dir_) == '#':
                dir_ *= self.TurnRight
            else:
                pos += dir_
        return (
            list(set(s[0] for s in seen)),
            (pos, dir_) in seen
        )

    # store the grid in a dictionary, to make bounds checks and navigation simple
    # start represents the starting position of the guard
    def parse(self, input):
        lines = input.split("\n")
        map_ = {
            -self.Up * y + x: lines[y][x]
            for y in range(len(lines))
            for x in range(len(lines[0]))
        }

        start = next(x for x in map_ if map_[x] == '^')
        
        return map_, start

if __name__ == "__main__":
    with open("input.txt","r") as f:
        input_data = f.read().strip()

    solution= Solution()

    print("one", solution.part_one(input_data))
    print("two:", solution.part_one(input_data))