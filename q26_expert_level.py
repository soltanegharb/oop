"""Question: Define a class Employee with a class method from_string that creates
an instance from a string in the format "name-salary".
Also, add a static method is_valid_salary to check if a salary is a positive number.
"""










# Iris solution
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, int(salary))

    @staticmethod
    def is_valid_salary(salary):
        return isinstance(salary, int) and salary > 0

# Create an instance using the class method
emp = Employee.from_string("John-50000")
print(emp.name)  # Output: John
print(emp.salary)  # Output: 50000

# Use the static method
print(Employee.is_valid_salary(50000))  # Output: True
print(Employee.is_valid_salary(-100))   # Output: False
