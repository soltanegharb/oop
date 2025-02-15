"""Question: Implement a class ImmutableSet that inherits from set
and overrides methods to make it immutable.
"""


# Iris solution
class ImmutableSet(set):
    def __init__(self, *args):
        super().__init__(*args)
        self._frozen = True

    def _immutable(self, *args, **kwargs):
        if self._frozen:
            raise TypeError("This set is immutable")

    add = _immutable
    remove = _immutable
    discard = _immutable
    pop = _immutable
    clear = _immutable
    update = _immutable
    intersection_update = _immutable
    difference_update = _immutable
    symmetric_difference_update = _immutable

# Create an instance and attempt to modify it
immut_set = ImmutableSet([1, 2, 3])
print(immut_set)  # Output: {1, 2, 3}
try:
    immut_set.add(4)
except TypeError as e:
    print(e)  # Output: This set is immutable
