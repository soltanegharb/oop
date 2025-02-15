"""Question: Create a class Config that uses the Borg pattern to ensure
all instances share the same state.
"""


# Iris solution
class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state

class Config(Borg):
    def __init__(self, **kwargs):
        super().__init__()
        self._shared_state.update(kwargs)

# Create instances and observe shared state
config1 = Config(a=1, b=2)
config2 = Config(c=3)
print(config1.__dict__)  # Output: {'a': 1, 'b': 2, 'c': 3}
print(config2.__dict__)  # Output: {'a': 1, 'b': 2, 'c': 3}
