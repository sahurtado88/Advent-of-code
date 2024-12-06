from functools import cmp_to_key

class Solution:
    def part_one(self, input_data):
        updates, comparer = self.parse(input_data)
        return sum(
            self.get_middle_page(pages)
            for pages in updates
            if self.sorted(pages, comparer)
        )

    def part_two(self, input_data):
        updates, comparer = self.parse(input_data)
        return sum(
            self.get_middle_page(sorted(pages, key=cmp_to_key(comparer)))
            for pages in updates
            if not self.sorted(pages, comparer)
        )

    def parse(self, input_data):
        parts = input_data.strip().split("\n\n")

        # Parse ordering rules
        ordering = set(parts[0].splitlines())

        # Create custom comparer function
        def comparer(p1, p2):
            return -1 if f"{p1}|{p2}" in ordering else 1

        # Parse updates
        updates = [line.split(",") for line in parts[1].splitlines()]
        return updates, comparer

    def get_middle_page(self, nums):
        return int(nums[len(nums) // 2])

    def sorted(self, pages, comparer):
        # Check if pages are sorted according to the custom comparer
        return pages == sorted(pages, key=cmp_to_key(comparer))


# Ejemplo de uso
input_data = """\
A|B
B|C

A,B,C
C,B,A
B,A,C"""

solution = Solution()
print("Parte Uno:", solution.part_one(input_data))  # Salida para PartOne
print("Parte Dos:", solution.part_two(input_data))  # Salida para PartTwo
