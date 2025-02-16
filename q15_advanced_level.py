"""Question: Define a class named Vehicle with attributes make, model, and year.
Create a subclass named ElectricVehicle that adds an attribute battery_capacity
 and a method charge.
"""










# Iris solution
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging {self.make} {self.model} with {self.battery_capacity} kWh battery")

# Create an instance of ElectricVehicle and call the charge method
ev = ElectricVehicle("Tesla", "Model S", 2020, 100)
ev.charge()  # Output: Charging Tesla Model S with 100 kWh battery
