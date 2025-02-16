"""Question: Implement a class Matrix that supports matrix addition and multiplication.
Override the __add__ and __mul__ methods.
"""










# Iris solution
class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = []
        for row1, row2 in zip(self.data, other.data):
            result.append([x + y for x, y in zip(row1, row2)])
        return Matrix(result)

    def __mul__(self, other):
        result = []
        for row in self.data:
            new_row = []
            for col in zip(*other.data):
                new_row.append(sum(x * y for x, y in zip(row, col)))
            result.append(new_row)
        return Matrix(result)

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

# Create instances and perform operations
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
print(m1 + m2)  # Output: Matrix with elements [[6, 8], [10, 12]]
print(m1 * m2)  # Output: Matrix with elements [[19, 22], [43, 50]]
