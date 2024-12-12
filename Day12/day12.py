from collections import defaultdict, deque
from typing import Dict, Set, Tuple

# Aliases for clarity
Region = Set[complex]

class Solution:
    
    UP = complex(0, 1)    # Equivalent to Complex.ImaginaryOne
    DOWN = complex(0, -1) # Equivalent to -Complex.ImaginaryOne
    LEFT = complex(-1, 0) # Equivalent to -1
    RIGHT = complex(1, 0) # Equivalent to 1

    def part_one(self, input: str) -> int:
        return self.calculate_fence_price(input, self.find_edges)

    def part_two(self, input: str) -> int:
        return self.calculate_fence_price(input, self.find_corners)

    def calculate_fence_price(self, input: str, measure) -> int:
        """Calculate the total fence price based on the region perimeter."""
        regions = self.get_regions(input)
        total_price = 0
        for region in set(regions.values()):  # Get distinct regions
            perimeter = 0
            for point in region:
                perimeter += measure(regions, point)
            total_price += len(region) * perimeter
        return total_price

    def find_edges(self, map: Dict[complex, Region], point: complex) -> int:
        """Finds the number of edges for a given point in a region."""
        perimeter = 0
        region = map[point]
        for direction in [self.RIGHT, self.DOWN, self.LEFT, self.UP]:
            if map.get(point + direction) != region:
                perimeter += 1
        return perimeter

    def find_corners(self, map: Dict[complex, Region], point: complex) -> int:
        """Finds the number of corners for a given point in a region."""
        corners = 0
        region = map[point]
        
        for du, dv in [(self.UP, self.RIGHT), (self.RIGHT, self.DOWN), (self.DOWN, self.LEFT), (self.LEFT, self.UP)]:
            # Check for the first type of corner
            if map.get(point + du) != region and map.get(point + dv) != region:
                corners += 1
            
            # Check for the second type of corner
            if map.get(point + du) == region and \
               map.get(point + dv) == region and \
               map.get(point + du + dv) != region:
                corners += 1
        
        return corners

    def get_regions(self, input: str) -> Dict[complex, Region]:
        """Maps the positions of plants in a garden to their corresponding regions."""
        lines = input.split("\n")
        garden = {x + y * self.DOWN: char for y, row in enumerate(lines) for x, char in enumerate(row)}
        
        positions = set(garden.keys())
        regions = {}
        
        while positions:
            pivot = positions.pop()  # Pick a starting point
            region = {pivot}  # Create a new region
            queue = deque([pivot])  # Flood-fill queue
            plant = garden[pivot]  # Type of plant at pivot position
            
            while queue:
                point = queue.popleft()
                regions[point] = region
                
                for direction in [self.UP, self.DOWN, self.LEFT, self.RIGHT]:
                    neighbor = point + direction
                    if neighbor in positions and garden.get(neighbor) == plant:
                        region.add(neighbor)
                        queue.append(neighbor)
                        positions.remove(neighbor)
        
        return regions

# Example usage
if __name__ == "__main__":
    solution = Solution()
    input_data = "....\n.##.\n.##.\n...."  # Example input
    print("Part One:", solution.part_one(input_data))
    print("Part Two:", solution.part_two(input_data))
