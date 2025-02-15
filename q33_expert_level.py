"""Question: Implement a class MetaSingleton using metaclasses to ensure
only one instance of the class can be created.
"""


# Iris solution
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=MetaSingleton):
    def __init__(self):
        self.value = None

# Demonstrate Singleton pattern using metaclass
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # Output: True
