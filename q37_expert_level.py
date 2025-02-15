"""Question: Create a class ImmutablePoint that represents an immutable point in 2D space.
Override the __setattr__ method to prevent modification of attributes after initialization.
"""


# Iris solution
class ImmutablePoint:
    def __init__(self, x, y):
        super().__setattr__('x', x)
        super().__setattr__('y', y)

    def __setattr__(self, key, value):
        raise AttributeError("Cannot modify immutable point")

# Create an instance and attempt to modify attributes
point = ImmutablePoint(1, 2)
print(point.x, point.y)  # Output: 1 2
try:
    point.x = 3
except AttributeError as e:
    print(e)  # Output: Cannot modify immutable point
