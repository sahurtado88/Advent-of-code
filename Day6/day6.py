from collections import defaultdict
from typing import Dict, Tuple, List, Set

# Alias para el tipo de mapa
Map = Dict[complex, str]

# Direcciones
UP = complex(0, 1)
TURN_RIGHT = -1j  # Girar a la derecha es una rotación de -90 grados en el plano complejo


def parse(input: str) -> Tuple[Map, complex]:
    """
    Convierte la entrada de texto en un mapa y encuentra la posición inicial del guardia.
    """
    lines = input.split("\n")
    mapa = {
        complex(x, -y): char
        for y in range(len(lines))
        for x in range(len(lines[0]))
        if (char := lines[y][x]) != ' '  # Filtra los espacios vacíos
    }
    start = next(pos for pos, char in mapa.items() if char == '^')
    return mapa, start


def walk(mapa: Map, start: complex) -> Tuple[Set[complex], bool]:
    """
    Simula el movimiento del guardia siguiendo las reglas dadas.
    Devuelve las posiciones visitadas y si el guardia entra en un ciclo.
    """
    seen = set()
    dire = UP
    pos = start

    while pos in map and (pos, dire) not in seen:
        seen.add((pos, dire))
        
        if map.get(pos + dire, '.') == '#':
            dire *= TURN_RIGHT  # Gira a la derecha
        else:
            pos += dire  # Avanza en la dirección actual
    
    positions = {s[0] for s in seen}  # Extrae solo las posiciones visitadas
    is_loop = (pos, dire) in seen
    return positions, is_loop


def part_one(input: str) -> int:
    """
    Calcula la cantidad de posiciones únicas visitadas por el guardia antes de salir del mapa.
    """
    map, start = parse(input)
    positions, _ = walk(map, start)
    return len(positions)


def part_two(input: str) -> int:
    """
    Calcula la cantidad de bucles que ocurren al colocar un obstáculo en cada posición visitada por el guardia.
    """
    map, start = parse(input)
    positions, _ = walk(map, start)
    loops = 0
    
    for block in positions:
        if map.get(block, '.') == '.':  # Asegurarse de que sea un espacio libre
            map[block] = '#'
            _, is_loop = walk(map, start)
            if is_loop:
                loops += 1
            map[block] = '.'  # Restaurar la posición original
    
    return loops


if __name__ == "__main__":
    # Entrada de ejemplo
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
    
    print("Parte 1 (Posiciones únicas visitadas):", part_one(input_data))
    print("Parte 2 (Número de bucles encontrados):", part_two(input_data))
