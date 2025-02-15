"""Question: Create a class named Employee with attributes name and salary.
Add a method to give a raise (increase the salary by a given percentage).
"""


# Iris solution
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)

# Create an instance and give a raise
employee = Employee("John", 50000)
employee.give_raise(10)
print(employee.salary)  # Output: 55000
