"""Question: Create a class named Account with attributes account_number
and balance. Add methods to deposit, withdraw, and transfer money to another account.
"""










# Iris solution
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.withdraw(amount)
            other_account.deposit(amount)
        else:
            print("Insufficient funds")

# Create instances and perform operations
acc1 = Account("12345", 1000)
acc2 = Account("67890", 500)
acc1.transfer(200, acc2)
print(acc1.balance)  # Output: 800
print(acc2.balance)  # Output: 700
