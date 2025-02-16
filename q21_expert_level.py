"""Question: Implement a class Polynomial that supports polynomial addition,
subtraction, and evaluation. Override the __add__, __sub__, and __call__ methods.
"""










# Iris solution
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        result = [a + b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

    def __sub__(self, other):
        result = [a - b for a, b in zip(self.coefficients, other.coefficients)]
        return Polynomial(result)

    def __call__(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

    def __str__(self):
        return " + ".join(f"{coef}x^{i}" for i, coef in enumerate(self.coefficients))

# Create instances and perform operations
p1 = Polynomial([1, 2, 3])  # Represents 1 + 2x + 3x^2
p2 = Polynomial([3, 2, 1])  # Represents 3 + 2x + 1x^2
print(p1 + p2)  # Output: Polynomial with coefficients [4, 4, 4]
print(p1 - p2)  # Output: Polynomial with coefficients [-2, 0, 2]
print(p1(2))    # Output: 17 (1 + 2*2 + 3*2^2)
