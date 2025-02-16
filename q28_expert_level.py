"""Question: Define a class Product with private attributes _name and _price.
Use properties to get and set these attributes with validation.
Add a method to apply a discount to the price.
"""










# Iris solution
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be a positive number")
        self._price = value

    def apply_discount(self, discount_percentage):
        if 0 < discount_percentage < 100:
            self._price -= self._price * (discount_percentage / 100)

# Create an instance and use properties and methods
product = Product("Laptop", 1000)
print(product.name)  # Output: Laptop
print(product.price)  # Output: 1000
product.apply_discount(10)
print(product.price)  # Output: 900
