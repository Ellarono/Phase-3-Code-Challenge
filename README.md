## School Management System
This is a Python-based application for managing students, courses, and their enrollments within a school. The project demonstrates the use of Object-Oriented Programming (OOP) concepts, including classes, relationships, and aggregate methods.


### Technologies Used
Python: Core programming language used for the application.

## File Structure
student.py: Contains the Student class, which handles student details and enrollments.
course.py: Contains the Course class, which manages course details and enrolled students.
school.py: Contains the School class, which aggregates and manages students and courses.
main.py: Entry point for testing and demonstrating the application.

## How to Run the Program
1. Clone the repository or download the files.
2. Navigate to the project directory in your terminal.
3. Run the program using the command:
```bash
python main.py
```
4. Follow the output in the terminal to interact with the program.
   
### Expected Output
When you run the program, you should see:

Confirmation of students being enrolled in courses.
A list of all students and courses in the school.
A list of students enrolled in a specific course.
Example:

``` less
Alice has been enrolled in Mathematics.
Bob has been enrolled in Physics.
Charlie has been enrolled in History.
Alice has been enrolled in Physics.

List of Students:
['Alice', 'Bob', 'Charlie']

List of Courses:
['Mathematics', 'Physics', 'History']

Students in Mathematics:
['Alice']
```
### Future Improvements
- Add functionality to remove students or courses.
- Handle duplicate enrollments more gracefully.
- Save and load data from a file for persistence.
