# Polymorphism Through Method Overloading-Like Behavior (Advanced)

# Python does not support traditional method overloading based on different parameter types or counts in the same way as Java or C++. However, we can achieve similar behavior using default arguments.

# Scenario: A calculator can add two or three numbers.


class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


calculator = Calculator()

print("Two numbers:", calculator.add(10, 20))

print("Three numbers:", calculator.add(10, 20, 30))


# - The same method handles different numbers of arguments.
# - The third parameter has a default value of zero.
# - This is an alternative to traditional method overloading.
# Key concept: Flexible method arguments.