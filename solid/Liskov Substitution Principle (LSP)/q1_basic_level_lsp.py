"""Question: Define a class Bird with a method fly.
Create subclasses Sparrow and Penguin.
Ensure that substituting a Penguin for a Bird does not violate
the Liskov Substitution Principle.
"""


# Iris solution
class Bird:
    def fly(self):
        raise NotImplementedError("Subclasses must implement this method")

class Sparrow(Bird):
    def fly(self):
        return "Sparrow is flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins cannot fly")

# Usage
birds = [Sparrow(), Penguin()]
for bird in birds:
    try:
        print(bird.fly())
    except Exception as e:
        print(e)
