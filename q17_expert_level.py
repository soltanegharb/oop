"""Question: Implement a class Vector that supports vector addition,
subtraction, and dot product. Override the __add__, __sub__, and __mul__ methods.
"""


# My solution
class Vector:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
    
    def __sub__(self, other_vector):
        return Vector(self.x_position - other_vector.x_position, self.y_position - other_vector.y_position)
    
    def __add__(self, other_vector):
        return Vector(self.x_position + other_vector.x_position, self.y_position + other_vector.y_position)
    
    def __mul__(self, other_vector):
        return Vector(self.x_position * other_vector.x_position, self.y_position * other_vector.y_position)
    
    def __str__(self):
        return f"Vector(x_position:{self.x_position}, y_position:{self.y_position})"
    
vec1 = Vector(x_position=10, y_position=11)
vec2 = Vector(x_position=5, y_position=6)
vec_difference = vec1 - vec2
vec_addition = vec1 + vec2
vec_multiplication = vec1 * vec2

print(vec1)
print(vec2)
print(vec_difference)
print(vec_addition)
print(vec_multiplication)


# Iris solution
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Create instances and perform operations
v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: Vector(6, 8)
print(v1 - v2)  # Output: Vector(-2, -2)
print(v1 * v2)  # Output: 23
