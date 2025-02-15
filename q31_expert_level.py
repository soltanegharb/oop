"""Question: Define a class Employee with a private attribute _salary.
Use a property to get and set the salary with validation.
Add a class method from_dict to create an instance from a dictionary and
a static method is_valid_employee_data to validate the dictionary data.
"""


# Iris solution
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Salary must be a positive number")
        self._salary = value

    @classmethod
    def from_dict(cls, data):
        if cls.is_valid_employee_data(data):
            return cls(data['name'], data['salary'])
        else:
            raise ValueError("Invalid employee data")

    @staticmethod
    def is_valid_employee_data(data):
        return 'name' in data and 'salary' in data and isinstance(data['salary'], (int, float)) and data['salary'] > 0

# Create an instance using the class method
emp_data = {'name': 'John', 'salary': 50000}
emp = Employee.from_dict(emp_data)
print(emp.name)  # Output: John
print(emp.salary)  # Output: 50000
