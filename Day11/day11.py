from functools import lru_cache
from collections import defaultdict

class Solution:
    
    def part_one(self, input: str) -> int:
        return self.stone_count(input, 25)

    def part_two(self, input: str) -> int:
        return self.stone_count(input, 75)

    def stone_count(self, input: str, blinks: int) -> int:
        """
        Splits the input by spaces, parses each part as an integer, and sums up the 
        total stones calculated for each part using the `eval` method.
        """
        cache = defaultdict(int)  # This simulates the cache in C#
        return sum(self.eval(int(n), blinks, cache) for n in input.split(" "))

    def eval(self, n: int, blinks: int, cache: dict) -> int:
        """
        Recursively calculates the total number of stones generated by a single engravement (n)
        after a specified number of blinks. Uses caching to optimize and prevent exponential
        computation by storing intermediate results.
        """
        if (str(n), blinks) in cache:
            return cache[(str(n), blinks)]
        
        if blinks == 0:
            return 1
        
        if n == 0:
            result = self.eval(1, blinks - 1, cache)
        elif len(str(n)) % 2 == 0:
            half_length = len(str(n)) // 2
            left_part = int(str(n)[:half_length])
            right_part = int(str(n)[half_length:])
            result = self.eval(left_part, blinks - 1, cache) + self.eval(right_part, blinks - 1, cache)
        else:
            result = self.eval(2024 * n, blinks - 1, cache)
        
        cache[(str(n), blinks)] = result
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    input_data = "6571 0 5851763 526746 23 69822 9 989"  # Example input
    print("Part One:", solution.part_one(input_data))
    print("Part Two:", solution.part_two(input_data))
