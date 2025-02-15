"""Question: Implement a class Shape with a method area that raises a NotImplementedError.
Create subclasses Circle and Rectangle that implement the area method.
Demonstrate polymorphism by creating a list of shapes and calculating their areas.
"""


# Iris solution
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Demonstrate polymorphism
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area: {shape.area()}")
