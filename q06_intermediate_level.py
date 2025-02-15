"""Question: Create a class named BankAccount with attributes account_number and balance.
Add methods to deposit and withdraw money, and to check the balance.
"""


from decimal import Decimal, getcontext


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        getcontext().prec = 2
        self._balance = Decimal(balance)

    @staticmethod
    def _check_correctness(amount):
        if amount > 0:
            return True

    def deposit(self, amount):
        amount = Decimal(amount)
        if self._check_correctness(amount):
            self._balance += amount
        else:
            raise ValueError

    def withdraw(self, amount):
        amount = Decimal(amount)
        if self._check_correctness(amount) and self._balance >= amount:
            self._balance -= amount
        else:
            raise ValueError

    def check_balance(self):
        return self._balance
    

ali_bank_melli_bazar = BankAccount('123456789', 50.00)
print(ali_bank_melli_bazar._balance)
ali_bank_melli_bazar.deposit(10.22)
print("deposited")
print(ali_bank_melli_bazar._balance)
ali_bank_melli_bazar.withdraw(10.23)
print("withdrawed")
print(ali_bank_melli_bazar._balance)
# ali_bank_melli_bazar.withdraw(10)
# print(ali_bank_melli_bazar._balance)
# ali_bank_melli_bazar.withdraw(100.22)
# print(ali_bank_melli_bazar._balance)
print(type(ali_bank_melli_bazar._balance))
print(ali_bank_melli_bazar._balance)


# Iris solution
class BankAccount:
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

    def check_balance(self):
        return self.balance

# Create an instance and perform transactions
account = BankAccount("123456")
account.deposit(1000)
account.withdraw(500)
print(account.check_balance())  # Output: 500
