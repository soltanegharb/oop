"""Question: Create a class named Shape with a method area that raises a
NotImplementedError. Create subclasses Circle and Square that implement the area method.
"""

from math import pi


# My solution
class Shape:
    def area(self):
        raise NotImplementedError('use child class area not mine!!!')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return self.radius * 2 * pi


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


sqare_ziba = Square(3)
print(sqare_ziba.area())

circle_ziba = Circle(3)
print(circle_ziba.area())


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

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Create instances and calculate areas
circle = Circle(5)
square = Square(4)
print(circle.area())  # Output: 78.53981633974483
print(square.area())  # Output: 16
