"""Question: Define a class named Car with attributes make, model, and year.
Create an instance of this class and print the attributes.
"""


# Iris solution
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Create an instance and print attributes
car = Car("Toyota", "Corolla", 2020)
print(car.make)
print(car.model)
print(car.year)
