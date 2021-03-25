
class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        for row in self.list_of_lists:
            for i in row:
                print(i, end=' ')
            print()

    def __add__(self, second):
        for i in range(len(self.list_of_lists)):
            for j in range(len(second.list_of_lists[i])):
                self.list_of_lists[i][j] = self.list_of_lists[i][j] + second.list_of_lists[i][j]
        return Matrix.__str__(self)


matrix_1 = Matrix([[3, 5, 32],
                   [2, 4, 6],
                   [-1, 64, -8]])

matrix_2 = Matrix([[-2, 0, 2],
                   [-2, 0, 2],
                   [0, 2, -2]])


print(matrix_1.__add__(matrix_2))
