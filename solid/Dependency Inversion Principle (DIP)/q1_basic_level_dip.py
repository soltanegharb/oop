"""Question: Define a class Light with a method turn_on.
Create a class Switch that depends on Light.
Refactor the classes to adhere to
the Dependency Inversion Principle by introducing an interface Switchable.
"""


# Iris solution
# Initial classes violating DIP
class Light:
    def turn_on(self):
        return "Light is on"

class Switch:
    def __init__(self, light):
        self.light = light

    def operate(self):
        return self.light.turn_on()

# Refactored classes adhering to DIP
from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Light(Switchable):
    def turn_on(self):
        return "Light is on"

class Switch:
    def __init__(self, device: Switchable):
        self.device = device

    def operate(self):
        return self.device.turn_on()

# Usage
light = Light()
switch = Switch(light)
print(switch.operate())  # Output: Light is on
