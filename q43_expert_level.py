"""Question: Implement a class LazyProperty that uses the descriptor protocol
to implement a property that is computed on first access and then cached.
"""


# Iris solution
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.value = None

    def __get__(self, instance, owner):
        if self.value is None:
            self.value = self.func(instance)
        return self.value

class MyClass:
    @LazyProperty
    def expensive_computation(self):
        print("Computing value")
        return 42

# Create an instance and access the lazy property
obj = MyClass()
print(obj.expensive_computation)  # Output: Computing value \n 42
print(obj.expensive_computation)  # Output: 42
