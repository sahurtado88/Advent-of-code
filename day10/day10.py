from collections import defaultdict, deque
from itertools import product


class Solution:
    def __init__(self):
        self.Up = 1j  # Equivalente a Complex.ImaginaryOne
        self.Down = -1j  # Equivalente a -Complex.ImaginaryOne
        self.Left = -1  # Equivalente a -1 en C#
        self.Right = 1  # Equivalente a 1 en C#

    def part_one(self, input_data):
        """Calcula la suma de las posiciones distintas de todas las rutas."""
        trails = self.get_all_trails(input_data)
        return sum(len(set(trail)) for trail in trails.values())

    def part_two(self, input_data):
        """Calcula la suma de la longitud de todas las rutas."""
        trails = self.get_all_trails(input_data)
        return sum(len(trail) for trail in trails.values())

    def get_all_trails(self, input_data):
        """Obtiene todos los senderos desde los puntos de partida."""
        map_data = self.get_map(input_data)
        trail_heads = self.get_trail_heads(map_data)
        return {t: self.get_trails_from(map_data, t) for t in trail_heads}

    def get_trail_heads(self, map_data):
        """Obtiene las posiciones de los puntos de partida donde el valor es '0'."""
        return [pos for pos, char in map_data.items() if char == '0']

    def get_trails_from(self, map_data, trail_head):
        """Realiza una búsqueda en anchura (floodfill) desde el punto de partida."""
        positions = deque([trail_head])  # Cola para la búsqueda en anchura
        trails = []  # Lista de posiciones que forman el camino
        visited = set()  # Conjunto de posiciones ya visitadas

        while positions:
            point = positions.popleft()
            if point in visited:
                continue
            visited.add(point)

            if map_data.get(point) == '9':
                trails.append(point)
            else:
                for direction in [self.Up, self.Down, self.Left, self.Right]:
                    neighbor = point + direction
                    if map_data.get(neighbor) == chr(ord(map_data[point]) + 1):
                        positions.append(neighbor)

        return trails

    def get_map(self, input_data):
        """Convierte la entrada en un mapa que almacena las posiciones y sus valores."""
        map_lines = input_data.strip().split("\n")
        map_data = {
            x + y * -1j: char  # x + y * -1j representa la posición como un número complejo
            for y, row in enumerate(map_lines)
            for x, char in enumerate(row)
        }
        return map_data


# Ejemplo de uso
if __name__ == "__main__":
    input_data = (
        "012\n"
        "345\n"
        "678"
    )
    solution = Solution()
    part_one_result = solution.part_one(input_data)
    part_two_result = solution.part_two(input_data)
    print(f"Parte 1: {part_one_result}")
    print(f"Parte 2: {part_two_result}")
