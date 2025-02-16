"""Question: Add a method display_info to the Car class that prints the car's make,
model, and year.
"""










# My solution
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"Car: make: {self.make}, model: {self.model}, year: {self.year}"


samand_car = Car(make='iran khodro', model='samand', year=1390)
print(samand_car.year)
print(samand_car.make)
print(samand_car.model)
print(samand_car.display_info())


#Iris solution
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.make} {self.model}, Year: {self.year}")

# Create an instance and call the display_info method
car = Car("Toyota", "Corolla", 2020)
car.display_info()
