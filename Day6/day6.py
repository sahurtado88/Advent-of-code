from typing import Dict, Tuple, List, Set, Iterable
from collections import defaultdict

# Tipo alias para facilitar la comprensión
Map = Dict[complex, str]  # Mapa de coordenadas (complejo) a caracteres

class Solution:
    def __init__(self):
        self.Up = complex(0, 1)  # Equivalente a Complex.ImaginaryOne
        self.TurnRight = -1j     # Equivalente a -Complex.ImaginaryOne

    def part_one(self, input: str) -> int:
        """Calcula el número de posiciones visitadas en la parte uno."""
        map_, start = self._parse(input)
        positions, _ = self._walk(map_, start)
        return len(positions)
    
    def part_two(self, input: str) -> int:
        """Cuenta el número de ciclos formados en la parte dos."""
        map_, start = self._parse(input)
        positions, _ = self._walk(map_, start)
        loops = 0
        
        # Intentar bloquear cada posición que sea un '.' y verificar si se forma un ciclo
        for block in [pos for pos in positions if map_[pos] == '.']:
            map_[block] = '#'
            _, is_loop = self._walk(map_, start)
            if is_loop:
                loops += 1
            map_[block] = '.'  # Restaurar el mapa original
        return loops

    def _walk(self, map_: Map, pos: complex) -> Tuple[Set[complex], bool]:
        """Simula el movimiento del guardia desde la posición inicial."""
        seen = set()
        dir_ = self.Up
        
        while pos in map_ and (pos, dir_) not in seen:
            seen.add((pos, dir_))
            
            if map_.get(pos + dir_, '#') == '#':  # Gira a la derecha si hay una pared
                dir_ *= self.TurnRight
            else:
                pos += dir_  # Mover en la dirección actual

        # Retorna las posiciones distintas que el guardia visitó y si se detectó un ciclo
        positions = {pos_dir[0] for pos_dir in seen}
        is_loop = (pos, dir_) in seen
        return positions, is_loop

    def _parse(self, input: str) -> Tuple[Map, complex]:
        """Parsea la entrada en un mapa de caracteres y la posición de inicio."""
        lines = input.split("\n")
        
        map_ = {
            complex(x, -y): char
            for y in range(len(lines))
            for x in range(len(lines[y]))
            for char in [lines[y][x]]
        }
        
        start = next(pos for pos, char in map_.items() if char == '^')
        
        return map_, start

# Ejemplo de uso
if __name__ == "__main__":
    input_data = """#####
#...#
#.^.#
#...#
#####"""
    
    solution = Solution()
    print("Part One:", solution.part_one(input_data))  # Calcula el número de posiciones visitadas
    print("Part Two:", solution.part_two(input_data))  # Calcula el número de ciclos detectados
