# student.py
class Student:
    def __init__(self, name):
        """
        Initialize a student with a name and an empty list of courses.
        """
        self.name = name
        self.courses = []  # List to store enrolled courses

    def enroll(self, course):
        """
        Enroll the student in a course.
        """
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)  # Add the student to the course as well
