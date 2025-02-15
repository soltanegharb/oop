"""Question: Implement a class ImmutableDict that inherits from dict
and overrides methods to make it immutable.
"""


# Iris solution
class ImmutableDict(dict):
    def __setitem__(self, key, value):
        raise TypeError("This dictionary is immutable")

    def __delitem__(self, key):
        raise TypeError("This dictionary is immutable")

    def clear(self):
        raise TypeError("This dictionary is immutable")

    def pop(self, key, default=None):
        raise TypeError("This dictionary is immutable")

    def popitem(self):
        raise TypeError("This dictionary is immutable")

    def update(self, *args, **kwargs):
        raise TypeError("This dictionary is immutable")

# Create an instance and attempt to modify it
immut_dict = ImmutableDict(a=1, b=2)
print(immut_dict)  # Output: {'a': 1, 'b': 2}
try:
    immut_dict['c'] = 3
except TypeError as e:
    print(e)  # Output: This dictionary is immutable
