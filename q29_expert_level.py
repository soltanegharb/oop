"""Question: Implement a class Vector that supports
vector addition, subtraction, and dot product.
Override the __add__, __sub__, and __mul__ methods.
Use encapsulation to ensure vectors are of the same length for these operations.
"""


# Iris solution
class Vector:
    def __init__(self, *components):
        self._components = components

    def __add__(self, other):
        if len(self._components) != len(other._components):
            raise ValueError("Vectors must be of the same length")
        result = [a + b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __sub__(self, other):
        if len(self._components) != len(other._components):
            raise ValueError("Vectors must be of the same length")
        result = [a - b for a, b in zip(self._components, other._components)]
        return Vector(*result)

    def __mul__(self, other):
        if len(self._components) != len(other._components):
            raise ValueError("Vectors must be of the same length")
        result = sum(a * b for a, b in zip(self._components, other._components))
        return result

    def __str__(self):
        return f"Vector{self._components}"

# Create instances and perform operations
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1 + v2)  # Output: Vector(5, 7, 9)
print(v1 - v2)  # Output: Vector(-3, -3, -3)
print(v1 * v2)  # Output: 32 (dot product)
