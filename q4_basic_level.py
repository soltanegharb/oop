"""Question: Add a method display_info to the Car class that prints the car's make,
model, and year.
"""


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
