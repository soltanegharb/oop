"""Question: Define a class named Car with attributes make, model, and year.
Create an instance of this class and print the attributes.
"""










# My solution
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


samand_car = Car(make='iran khodro', model='samand', year=1390)
print(samand_car.year)
print(samand_car.make)
print(samand_car.model)


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
