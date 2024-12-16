import re
from typing import List, Tuple, Generator

class Vec2:
    """Representa un vector 2D con coordenadas x e y."""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vec2(x={self.x}, y={self.y})"


class Solution:
    """Solución para el problema 'Claw Contraption'."""

    def part_one(self, input: str) -> int:
        """Resuelve la Parte 1 del problema."""
        return sum(self.get_prize(machine) for machine in self.parse(input))

    def part_two(self, input: str) -> int:
        """Resuelve la Parte 2 del problema con un desplazamiento (shift) aplicado."""
        return sum(self.get_prize(machine) for machine in self.parse(input, shift=10_000_000_000_000))

    def get_prize(self, machine: Tuple[Vec2, Vec2, Vec2]) -> int:
        """Calcula el premio basado en la solución del sistema de ecuaciones."""
        a, b, p = machine

        # Resuelve a * i + b * j = p para i y j usando la regla de Cramer
        i = self.det(p, b) // self.det(a, b)  # División entera
        j = self.det(a, p) // self.det(a, b)  # División entera

        # Devuelve el premio cuando se encuentra una solución entera no negativa
        if i >= 0 and j >= 0 and a.x * i + b.x * j == p.x and a.y * i + b.y * j == p.y:
            return 3 * i + j
        else:
            return 0

    def det(self, a: Vec2, b: Vec2) -> int:
        """Calcula el determinante de dos vectores 2D."""
        return a.x * b.y - a.y * b.x

    def parse(self, input: str, shift: int = 0) -> Generator[Tuple[Vec2, Vec2, Vec2], None, None]:
        """Parsea el input para producir una lista de 'máquinas' representadas por tuplas de tres vectores 2D."""
        blocks = input.split("\n\n")
        for block in blocks:
            nums = [int(num) for num in re.findall(r"\d+", block)]
            
            # Agrupa los números en pares y crea objetos Vec2
            vecs = [Vec2(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]
            
            # Aplica el desplazamiento al tercer vector
            vecs[2] = Vec2(vecs[2].x + shift, vecs[2].y + shift)
            yield (vecs[0], vecs[1], vecs[2])


# Ejemplo de uso
if __name__ == "__main__":
    input_data = """1, 2\n3, 4\n5, 6\n\n7, 8\n9, 10\n11, 12"""
    solution = Solution()
    print("Parte 1:", solution.part_one(input_data))
    print("Parte 2:", solution.part_two(input_data))
