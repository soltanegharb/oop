"""Question: Create a class CustomList that inherits from list and 
overrides the __getitem__ and __setitem__ methods to add custom behavior
(e.g., logging access and modifications).
"""


# Iris solution
class CustomList(list):
    def __getitem__(self, index):
        print(f"Accessing index {index}")
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        print(f"Setting index {index} to {value}")
        super().__setitem__(index, value)

# Create an instance and perform operations
custom_list = CustomList([1, 2, 3])
print(custom_list[1])  # Output: Accessing index 1 \n 2
custom_list[1] = 42  # Output: Setting index 1 to 42
print(custom_list)  # Output: [1, 42, 3]
