"""Question: Define a class Memento that uses the Memento pattern to capture
and restore an object's state.
"""


# Iris solution
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def save_state(self):
        return Memento(self._state)

    def restore_state(self, memento):
        self._state = memento.get_state()

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

# Use the Memento pattern
originator = Originator("State1")
memento = originator.save_state()
originator.set_state("State2")
print(originator.get_state())  # Output: State2
originator.restore_state(memento)
print(originator.get_state())  # Output: State1
