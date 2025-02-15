"""Question: Define a class Person with private attributes _name and _age.
Use properties to get and set these attributes with validation
(e.g., age must be a positive integer).
"""


# Iris solution
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer")
        self._age = value

# Create an instance and use properties
person = Person("Alice", 30)
print(person.name)  # Output: Alice
print(person.age)   # Output: 30
person.age = 35
print(person.age)   # Output: 35
