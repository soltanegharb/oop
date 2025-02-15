"""Question: Create a class named Course with attributes course_name and students
(a list of student names). Add methods to enroll a student, drop a student,
and list all students.
"""


# Iris solution
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)

    def drop_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)

    def list_students(self):
        return self.students

# Create an instance and perform operations
course = Course("Python Programming")
course.enroll_student("Alice")
course.enroll_student("Bob")
course.drop_student("Alice")
print(course.list_students())  # Output: ['Bob']
