"""Question: Define a class named Animal with attributes name and species.
Create a subclass named Dog that adds an attribute breed and a method bark.
"""


# Iris solution
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print("Woof!")

# Create an instance of Dog and call the bark method
dog = Dog("Buddy", "Canine", "Golden Retriever")
dog.bark()  # Output: Woof!
