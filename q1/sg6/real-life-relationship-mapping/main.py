# Write a short Python code snippet showing a Course adding a Student object to a list. 
class Student:
    def __init__(self, student_id : str, name : str):
        self.student_id = student_id
        self.name = name
    
    def enrollInCourse(self, course):
        course.add_student(self)

class Course:
    def __init__(self, course_id : str, title : str):
        self.course_id = course_id
        self.title = title
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_students(self):
        return self.students

student1 = Student("S001", "Kyren")
course1 = Course("C001", "Introduction to Nuclear Science")

course1.add_student(student1)

for student in course1.get_students():
    print(f"Student ID: {student.student_id}, Name: {student.name}")
    print("Student ID:", student.student_id, "Name:", student.name)
