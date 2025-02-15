"""Question: Add a method greet to the Person class that prints
a greeting message including the person's name.
"""


# My solution
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return self.name

farshad = Person(name='Farshad', age=18)
print(farshad.name)
print(farshad.age)
print(f'hello {farshad.greet()}, howdy')


# Iris solution
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Create an instance and call the greet method
person = Person("Alice", 30)
person.greet()
