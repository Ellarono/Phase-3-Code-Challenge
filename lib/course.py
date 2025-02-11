# course.py
class Course:
    def __init__(self, name):
        """
        Initialize a course with a name and an empty list of enrolled students.
        """
        self.name = name
        self.students = []  # List to store enrolled students

    def add_student(self, student):
        """
        Add a student to the course.
        """
        if student not in self.students:
            self.students.append(student)

    def list_students(self):
        """
        List all students enrolled in the course.
        """
        return [student.name for student in self.students]
