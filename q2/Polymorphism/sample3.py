# Polymorphism Through Inheritance and Method Overriding
# Different employees have different ways of calculating their salary.

class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        return 0


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 30000


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 15000


class ContractEmployee(Employee):
    def calculate_salary(self):
        return 20000


# Object creation
employees = [FullTimeEmployee("John"), PartTimeEmployee("Mark"), ContractEmployee("Anna")]
# from right to left side [-3,-2,-1]
#from left right ->  0,1,2

# Polymorphism
for employee in employees:
    print(employee.name, "Salary:", employee.calculate_salary())





# Employee is the parent class.
# The three employee types inherit from Employee.
# Each child class overrides calculate_salary().
# Python executes the appropriate overridden method based on the actual object.