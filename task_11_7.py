class CompNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма: {self.a + other.a} + {self.b + other.b} * j + i'

    def __mul__(self, other):
        return f'Произведение: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * x'


comp_1 = CompNum(-10, 32)
comp_2 = CompNum(56, 3)

print(comp_1 + comp_2)
print(comp_1 * comp_2)
