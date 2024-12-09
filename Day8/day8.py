from typing import List, Dict, Set, Callable, Iterable
from collections import defaultdict

# Tipo alias para facilitar la comprensión
Map = Dict[complex, str]  # Mapa de coordenadas (complejo) a caracteres

class Solution:
    
    def part_one(self, input: str) -> int:
        """Calcula el número de posiciones únicas para la parte uno."""
        return len(self._get_unique_positions(input, self._get_antinodes1))
    
    def part_two(self, input: str) -> int:
        """Calcula el número de posiciones únicas para la parte dos."""
        return len(self._get_unique_positions(input, self._get_antinodes2))
    
    def _get_unique_positions(self, input: str, get_antinodes: Callable[[complex, complex, Map], Iterable[complex]]) -> Set[complex]:
        """Obtiene las posiciones únicas de los antinodos de acuerdo con la lógica de la parte 1 o 2."""
        map_ = self._get_map(input)
        
        # Encuentra las posiciones de las "antenas" (letras o dígitos)
        antenna_locations = [pos for pos in map_ if map_[pos].isalnum()]
        
        unique_positions = {
            antinode 
            for src_antenna in antenna_locations 
            for dst_antenna in antenna_locations 
            if src_antenna != dst_antenna and map_[src_antenna] == map_[dst_antenna]
            for antinode in get_antinodes(src_antenna, dst_antenna, map_)
        }
        
        return unique_positions

    def _get_antinodes1(self, src_antenna: complex, dst_antenna: complex, map_: Map) -> Iterable[complex]:
        """Para la parte 1, busca el nodo antinodo inmediato."""
        direction = dst_antenna - src_antenna
        antinode = dst_antenna + direction
        if antinode in map_:
            yield antinode

    def _get_antinodes2(self, src_antenna: complex, dst_antenna: complex, map_: Map) -> Iterable[complex]:
        """Para la parte 2, busca una secuencia de antinodos cíclicos, comenzando desde dst_antenna."""
        direction = dst_antenna - src_antenna
        antinode = dst_antenna
        while antinode in map_:
            yield antinode
            antinode += direction

    def _get_map(self, input: str) -> Map:
        """Crea un mapa de coordenadas complejas a caracteres a partir de la entrada."""
        map_ = {}
        for y, row in enumerate(input.split("\n")):
            for x, char in enumerate(row):
                position = complex(x, -y)  # (x - yj) en C# se traduce a complex(x, -y) en Python
                map_[position] = char
        return map_

# Ejemplo de uso
if __name__ == "__main__":
    input_data = """A..B
                    .#..
                    C..D"""
    
    solution = Solution()
    print("Part One:", solution.part_one(input_data))  # Calcula la cantidad de posiciones únicas para la parte 1
    print("Part Two:", solution.part_two(input_data))  # Calcula la cantidad de posiciones únicas para la parte 2
