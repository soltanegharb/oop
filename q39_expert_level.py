"""Question: Create a class ObservableProperty that uses the descriptor
protocol to notify observers when a property value changes.
"""


# Iris solution
class ObservableProperty:
    def __init__(self, initial_value=None):
        self.value = initial_value
        self.observers = []

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value
        for observer in self.observers:
            observer(value)

    def add_observer(self, observer):
        self.observers.append(observer)

class MyClass:
    prop = ObservableProperty()

# Create an instance and add observers
def observer(value):
    print(f"Property changed to {value}")

obj = MyClass()
obj.prop.add_observer(observer)
obj.prop = 42  # Output: Property changed to 42
