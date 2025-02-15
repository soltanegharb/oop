"""Question: Define a class Flyweight that uses the Flyweight pattern
to minimize memory usage by sharing common data between instances.
"""


# Iris solution
class Flyweight:
    _instances = {}

    def __new__(cls, shared_state):
        if shared_state not in cls._instances:
            cls._instances[shared_state] = super(Flyweight, cls).__new__(cls)
            cls._instances[shared_state].shared_state = shared_state
        return cls._instances[shared_state]

# Create instances and observe shared state
fw1 = Flyweight("shared")
fw2 = Flyweight("shared")
fw3 = Flyweight("unique")
print(fw1 is fw2)  # Output: True
print(fw1 is fw3)  # Output: False
