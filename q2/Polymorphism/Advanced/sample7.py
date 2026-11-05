class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def display(self):
        print("Result:", self.value)


num1 = Number(10)
num2 = Number(20)

result = num1 + num2

result.display()



# __add__() is a special method in Python.
# It defines what happens when the + operator is used between two Number objects.
# Python internally calls num1.__add__(num2)