class Cell:
    def __init__(self, structure):
        self.structure = int(structure)

    def __add__(self, second):
        return self.structure + second.structure

    def __sub__(self, second):
        return self.structure - second.structure

    def __truediv__(self, second):
        return self.structure // second.structure

    def __mul__(self, second):
        return self.structure * second.structure

    def make_order(self, row):
        result = ''
        for i in range(int(self.structure / row)):
            result += '*' * row + '\n'
        result += '*' * (self.structure % row) + '\n'
        return result


cell_1 = Cell(18)
cell_2 = Cell(12)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(5))
