# Polymorphism Through Duck Typing (Intermediate)
# Scenario: Different objects can perform an action even if they do not inherit from the same parent class.

class PDF:
    def open(self):
        print("Opening PDF document...")


class Word:
    def open(self):
        print("Opening Word document...")


class Image:
    def open(self):
        print("Displaying image...")


# Objects
files = [PDF(), Word(), Image()]

# Polymorphism
for file in files:
    file.open()



# Python follows the principle:
# "If an object behaves like a duck, it can be treated like a duck."
# The objects do not need to share a parent class. They only need to provide the method being called.
# Key concept: Duck typing.