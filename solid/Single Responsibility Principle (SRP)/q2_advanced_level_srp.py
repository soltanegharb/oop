"""Question: Create a class Order that handles order processing and payment.
Refactor the class to adhere to the Single Responsibility Principle
by separating order processing from payment processing.
"""


# Iris solution
# Initial class violating SRP
class Order:
    def __init__(self, items, payment_method):
        self.items = items
        self.payment_method = payment_method

    def process_order(self):
        # Process order items
        pass

    def process_payment(self):
        # Process payment
        pass

# Refactored classes adhering to SRP
class OrderProcessing:
    def __init__(self, items):
        self.items = items

    def process_order(self):
        # Process order items
        pass

class PaymentProcessing:
    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self):
        # Process payment
        pass

# Usage
order_processing = OrderProcessing(["item1", "item2"])
payment_processing = PaymentProcessing("credit_card")
order_processing.process_order()
payment_processing.process_payment()
