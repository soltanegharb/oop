"""Question: Define a class named Rectangle with attributes length and width.
Add methods to calculate the area and perimeter of the rectangle.
"""


# My solution
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area_calculator(self):
        return self.length * self.width
    
    def perimeter_calculator(self):
        return (self.length + self.width) * 2


rect1 = Rectangle(10, 4)
print(rect1.width)
print(rect1.width)
print(rect1.area_calculator())
print(rect1.perimeter_calculator())


# Iris solution
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create an instance and calculate area and perimeter
rectangle = Rectangle(5, 3)
print(rectangle.area())       # Output: 15
print(rectangle.perimeter())  # Output: 16
