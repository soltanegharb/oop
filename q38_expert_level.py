"""Question: Define a class Resource that uses the context management protocol
(__enter__ and __exit__ methods) to manage resources.
Ensure that resources are properly acquired and released.
"""


# Iris solution
class Resource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Releasing resource")

# Use the context management protocol
with Resource() as resource:
    print("Using resource")
