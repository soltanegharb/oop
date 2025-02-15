"""Question: Create a class Strategy that uses the Strategy pattern to define
a family of algorithms. Implement strategies for Addition and Subtraction.
"""


# Iris solution
class Strategy:
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement this method")

class Addition(Strategy):
    def execute(self, a, b):
        return a + b

class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)

# Use the Strategy pattern
context = Context(Addition())
print(context.execute_strategy(5, 3))  # Output: 8
context.set_strategy(Subtraction())
print(context.execute_strategy(5, 3))  # Output: 2
