"""Question: Implement a class State that uses the State pattern to
change its behavior when its internal state changes.
"""


# Iris solution
class State:
    def handle(self):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteStateA(State):
    def handle(self):
        return "State A handling request"

class ConcreteStateB(State):
    def handle(self):
        return "State B handling request"

class Context:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def request(self):
        return self._state.handle()

# Use the State pattern
context = Context(ConcreteStateA())
print(context.request())  # Output: State A handling request
context.set_state(ConcreteStateB())
print(context.request())  # Output: State B handling request
