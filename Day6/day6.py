class AdventOfCodeY2024Day05:

    @staticmethod
    def part_one(input: str) -> int:
        updates, comparer = AdventOfCodeY2024Day05.parse(input)
        return sum(
            AdventOfCodeY2024Day05.get_middle_page(pages)
            for pages in updates
            if AdventOfCodeY2024Day05.sorted_pages(pages, comparer)
        )

    @staticmethod
    def part_two(input: str) -> int:
        updates, comparer = AdventOfCodeY2024Day05.parse(input)
        return sum(
            AdventOfCodeY2024Day05.get_middle_page(
                sorted(pages, key=cmp_to_key(comparer))
            )
            for pages in updates
            if not AdventOfCodeY2024Day05.sorted_pages(pages, comparer)
        )

    @staticmethod
    def parse(input: str) -> Tuple[List[List[str]], callable]:
        grid = input.strip().split("\n")
        
        # Crear un conjunto para representar alguna relación de orden (ajustar según el problema)
        ordering = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "#":
                    ordering.add(f"{row},{col}")

        def comparer(p1, p2):
            return -1 if f"{p1}|{p2}" in ordering else 1

        updates = [list(row) for row in grid]
        return updates, comparer

    @staticmethod
    def get_middle_page(nums: List[str]) -> int:
        # Asume que `nums` es un listado de caracteres de la fila del mapa, ajustar si es necesario
        return len(nums) // 2

    @staticmethod
    def sorted_pages(pages: List[str], comparer: callable) -> bool:
        return pages == sorted(pages, key=cmp_to_key(comparer))


# Ejemplo de uso con la entrada proporcionada
input_data = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

solution = AdventOfCodeY2024Day05
print("Part One:", solution.part_one(input_data))  # Ajustar lógica según el propósito
print("Part Two:", solution.part_two(input_data))  # Ajustar lógica según el propósito
