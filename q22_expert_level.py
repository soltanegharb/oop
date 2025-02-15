"""Question: Create a class StatefulObject that maintains an internal
state and allows state transitions.
Implement methods to get the current state, set a new state, and define valid transitions.
"""


# Iris solution
class StatefulObject:
    def __init__(self, initial_state):
        self.state = initial_state
        self.valid_transitions = {}

    def add_transition(self, from_state, to_state):
        if from_state not in self.valid_transitions:
            self.valid_transitions[from_state] = []
        self.valid_transitions[from_state].append(to_state)

    def set_state(self, new_state):
        if new_state in self.valid_transitions.get(self.state, []):
            self.state = new_state
        else:
            print(f"Invalid transition from {self.state} to {new_state}")

    def get_state(self):
        return self.state

# Create an instance and define state transitions
obj = StatefulObject("idle")
obj.add_transition("idle", "running")
obj.add_transition("running", "stopped")
obj.set_state("running")  # Valid transition
print(obj.get_state())    # Output: running
obj.set_state("stopped")  # Valid transition
print(obj.get_state())    # Output: stopped
obj.set_state("idle")     # Invalid transition
