"""Question: Create a class named Student with attributes name and grades
(a list of grades). Add methods to calculate the average grade and to add a new grade.
"""


# Iris solution
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

# Create an instance and perform operations
student = Student("Alice")
student.add_grade(90)
student.add_grade(85)
print(student.average_grade())  # Output: 87.5
