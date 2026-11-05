# A school system has different types of users: Students, Teachers, and Administrators. Each user has a different dashboard.

class User:

    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name

    def display_dashboard(self):
        print("Displaying general dashboard.")


class Student(User):

    def display_dashboard(self):
        print(f"Student {self.get_name()}:")
        print("Viewing grades and class schedules.")


class Teacher(User):

    def display_dashboard(self):
        print(f"Teacher {self.get_name()}:")
        print("Managing classes and student grades.")


class Administrator(User):

    def display_dashboard(self):
        print(f"Administrator {self.get_name()}:")
        print("Managing users and school records.")


# Creating objects
users = [
    Student("John"),
    Teacher("Maria"),
    Administrator("Mark")
]


# Polymorphism
for user in users:
    user.display_dashboard()
    print("--------------------")



# - User is the parent class.
# - Student, Teacher, and Administrator are child classes.
# - Each child class overrides display_dashboard().
# - The __name attribute is private.
# - get_name() provides controlled access to the private attribute.
# - A single loop executes different dashboard behaviors.
# Key concept: Combining encapsulation, inheritance, and polymorphism.