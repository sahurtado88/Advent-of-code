from collections import namedtuple

Block = namedtuple('Block', ['file_id', 'length'])


class Solution:
    def part_one(self, input_data):
        """Calcula la respuesta para la parte uno."""
        return self.checksum(self.compact_fs(self.parse(input_data), fragments_enabled=True))

    def part_two(self, input_data):
        """Calcula la respuesta para la parte dos."""
        return self.checksum(self.compact_fs(self.parse(input_data), fragments_enabled=False))

    def compact_fs(self, fs, fragments_enabled):
        """Mueve los bloques usados al inicio del disco."""
        i, j = 0, len(fs) - 1
        while i < j:
            if fs[i].file_id != -1:
                i += 1
            elif fs[j].file_id == -1:
                j -= 1
            else:
                self.relocate_block(fs, i, j, fragments_enabled)
                j -= 1
        return fs

    def relocate_block(self, fs, start, j, fragments_enabled):
        """Reubica el contenido del bloque `j` a un espacio libre que se encuentra después del nodo `start`."""
        for i in range(start, j):
            if fs[i].file_id != -1:
                continue
            elif fs[i].length == fs[j].length:
                fs[i], fs[j] = fs[j], fs[i]
                return
            elif fs[i].length > fs[j].length:
                d = fs[i].length - fs[j].length
                fs[i] = Block(fs[j].file_id, fs[j].length)
                fs[j] = Block(-1, fs[j].length)
                fs.insert(i + 1, Block(-1, d))
                return
            elif fs[i].length < fs[j].length and fragments_enabled:
                d = fs[j].length - fs[i].length
                fs[i] = Block(fs[j].file_id, fs[i].length)
                fs[j] = Block(fs[j].file_id, d)
                fs.insert(j + 1, Block(-1, fs[i].length))

    def checksum(self, fs):
        """Calcula el checksum de la lista de bloques."""
        res = 0
        l = 0
        for block in fs:
            for _ in range(block.length):
                if block.file_id != -1:
                    res += l * block.file_id
                l += 1
        return res

    def parse(self, input_data):
        """Parses the input into a list of Block objects."""
        return [Block(-1 if i % 2 == 1 else i // 2, int(ch)) for i, ch in enumerate(input_data)]


# Ejemplo de uso
if __name__ == "__main__":
    input_data = "1234567890"
    solution = Solution()
    part_one_result = solution.part_one(input_data)
    part_two_result = solution.part_two(input_data)
    print(f"Parte 1: {part_one_result}")
    print(f"Parte 2: {part_two_result}")
