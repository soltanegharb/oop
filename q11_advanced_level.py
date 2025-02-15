"""Question: Define a class named Employee with attributes name and salary.
Create a subclass named Manager that inherits from Employee and adds an attribute
department. Override the __str__ method to print the details of the manager.
"""

# My solution
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    
    def __str__(self):
        return f'Manager=\"{self.name}\", salary={self.salary}, department=\"{self.department}\"'


manager_ali = Manager(name='Ali', salary=10_000, department='Kobra 11')
print(manager_ali)


# Iris solution
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def __str__(self):
        return f"Manager: {self.name}, Department: {self.department}, Salary: {self.salary}"

# Create an instance of Manager and print details
manager = Manager("Bob", 80000, "IT")
print(manager)  # Output: Manager: Bob, Department: IT, Salary: 80000
