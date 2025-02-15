"""Question: Create a class BankAccount with protected attributes _account_number
and _balance. Add methods to deposit, withdraw, and check the balance.
Use encapsulation to ensure balance cannot be negative.
"""


# Iris solution
class BankAccount:
    def __init__(self, account_number, balance=0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

# Create an instance and perform operations
account = BankAccount("12345", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300
