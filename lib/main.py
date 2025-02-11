# main.py
from school import School

def main():
    # Step 1: Create a school
    my_school = School("Code Academy")

    # Step 2: Add students
    my_school.add_student("Alice")
    my_school.add_student("Bob")
    my_school.add_student("Charlie")

    # Step 3: Add courses
    my_school.add_course("Mathematics")
    my_school.add_course("Physics")
    my_school.add_course("History")

    # Step 4: Enroll students in courses
    print(my_school.enroll_student_in_course("Alice", "Mathematics"))
    print(my_school.enroll_student_in_course("Bob", "Physics"))
    print(my_school.enroll_student_in_course("Charlie", "History"))
    print(my_school.enroll_student_in_course("Alice", "Physics"))

    # Step 5: List all students
    print("\nList of Students:")
    print(my_school.list_students())

    # Step 6: List all courses
    print("\nList of Courses:")
    print(my_school.list_courses())

    # Step 7: Check course enrollments
    print("\nStudents in Mathematics:")
    for course in my_school.courses:
        if course.name == "Mathematics":
            print(course.list_students())

if __name__ == "__main__":
    main()
