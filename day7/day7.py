import re
from typing import List, Callable

class Solution:
    
    def part_one(self, input: str) -> int:
        """Calcula la suma de los objetivos que cumplen la condición de Check1."""
        return sum(self._filter(input, self._check1))
    
    def part_two(self, input: str) -> int:
        """Calcula la suma de los objetivos que cumplen la condición de Check2."""
        return sum(self._filter(input, self._check2))
    
    def _filter(self, input: str, check: Callable[[int, int, List[int]], bool]) -> List[int]:
        """
        Filtra las calibraciones válidas de acuerdo con la función de verificación proporcionada.
        """
        results = []
        for line in input.split("\n"):
            if line.strip():  # Para evitar líneas vacías
                parts = list(map(int, re.findall(r'\d+', line)))
                target = parts[0]
                nums = parts[1:]
                if check(target, nums[0], nums[1:]):
                    results.append(target)
        return results

    def _check1(self, target: int, acc: int, nums: List[int]) -> bool:
        """
        Recorre los números y utiliza las operaciones permitidas (* y +) para actualizar el resultado acumulado.
        """
        if not nums:
            return target == acc
        return (
            self._check1(target, acc * nums[0], nums[1:]) or 
            self._check1(target, acc + nums[0], nums[1:])
        )

    def _check2(self, target: int, acc: int, nums: List[int]) -> bool:
        """
        Recorre los números y usa concatenación, multiplicación y suma para alcanzar el objetivo.
        Se optimiza con una condición de salida temprana si acc > target.
        """
        if acc > target:  # Optimización: salida temprana si el acumulador supera el objetivo
            return False
        if not nums:
            return target == acc
        return (
            self._check2(target, int(f"{acc}{nums[0]}"), nums[1:]) or 
            self._check2(target, acc * nums[0], nums[1:]) or 
            self._check2(target, acc + nums[0], nums[1:])
        )

# Ejemplo de uso
if __name__ == "__main__":
    input_data = """123 4 5 6
                    42 2 2 2
                    10 2 2 2"""
    
    solution = Solution()
    print("Part One:", solution.part_one(input_data))
    print("Part Two:", solution.part_two(input_data))
