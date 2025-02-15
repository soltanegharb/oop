"""Question: Create a class Vehicle with a method start_engine.
Implement subclasses Car and Bicycle.
Ensure that substituting a Bicycle for a Vehicle does not violate
the Liskov Substitution Principle.
"""


# Iris solution
class Vehicle:
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started"

class Bicycle(Vehicle):
    def start_engine(self):
        raise Exception("Bicycles do not have engines")

# Usage
vehicles = [Car(), Bicycle()]
for vehicle in vehicles:
    try:
        print(vehicle.start_engine())
    except Exception as e:
        print(e)
