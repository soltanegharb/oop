"""Question: Define a class MetaLogger using a metaclass to automatically log
the creation of any instance of classes that use this metaclass.
"""


# Iris solution
class MetaLogger(type):
    def __call__(cls, *args, **kwargs):
        instance = super(MetaLogger, cls).__call__(*args, **kwargs)
        print(f"Created instance of {cls.__name__}")
        return instance

class MyClass(metaclass=MetaLogger):
    def __init__(self, value):
        self.value = value

# Create an instance and observe logging
obj = MyClass(10)  # Output: Created instance of MyClass
