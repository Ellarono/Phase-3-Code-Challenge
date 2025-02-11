# school.py
from student import Student
from course import Course

class School:
    def __init__(self, name):
        """
        Initialize a school with a name, and empty lists for students and courses.
        """
        self.name = name
        self.students = []  # List to store students
        self.courses = []   # List to store courses

    def add_student(self, student_name):
        """
        Add a new student to the school.
        """
        student = Student(student_name)
        self.students.append(student)
        return student

    def add_course(self, course_name):
        """
        Add a new course to the school.
        """
        course = Course(course_name)
        self.courses.append(course)
        return course

    def enroll_student_in_course(self, student_name, course_name):
        """
        Enroll a student in a course.
        """
        # Find the student and course objects
        student = next((s for s in self.students if s.name == student_name), None)
        course = next((c for c in self.courses if c.name == course_name), None)

        if student and course:
            student.enroll(course)
            return f"{student_name} has been enrolled in {course_name}."
        elif not student:
            return f"Student {student_name} not found."
        elif not course:
            return f"Course {course_name} not found."

    def list_students(self):
        """
        List all students in the school.
        """
        return [student.name for student in self.students]

    def list_courses(self):
        """
        List all courses in the school.
        """
        return [course.name for course in self.courses]
