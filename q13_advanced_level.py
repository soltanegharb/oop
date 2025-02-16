"""Question: Define a class named Animal with attributes name and species.
Create a subclass named Dog that adds an attribute breed and a method bark.
"""










# My solution
class Animal:
    species = None
    def __init__(self, name:str):
        self.name = name


class Dog(Animal):
    species = 'Mammals'
    def __init__(self, name:str, breed:str):
        super().__init__(name)
        self.breed = breed
    
    @staticmethod
    def bark():
        return f'hop hop hoppp'


jessi = Dog('jessi', 'german')
print(jessi.species)
print(jessi.bark())


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
