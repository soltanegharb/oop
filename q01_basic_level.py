"""Question: Define a class named Person with attributes name and age.
Create an instance of this class and print the attributes.
"""

# My solution
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


farshad = Person(name='Farshad', age=18)
print(farshad.name)
print(farshad.age)


# Iris Solution
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance and print attributes
person = Person("Alice", 30)
print(person.name)
print(person.age)
