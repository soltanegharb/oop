"""Question: Create a class Discount with a method apply_discount.
Implement subclasses PercentageDiscount and FixedAmountDiscount
that apply different types of discounts. 
Ensure the classes are open for extension but closed for modification.
"""


# Iris solution
class Discount:
    def apply_discount(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, amount):
        return amount - (amount * self.percentage / 100)

class FixedAmountDiscount(Discount):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, amount):
        return amount - self.discount_amount

# Usage
discounts = [PercentageDiscount(10), FixedAmountDiscount(20)]
amount = 100
for discount in discounts:
    print(f"Discounted amount: {discount.apply_discount(amount)}")
