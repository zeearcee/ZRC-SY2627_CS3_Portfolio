# Polymorphism Using a For Loop

class Dog:
    def make_sound(self):
        print("Woof! Woof!")


class Cat:
    def make_sound(self):
        print("Meow! Meow!")


class Cow:
    def make_sound(self):
        print("Moo! Moo!")


# Creating objects
dog = Dog()
cat = Cat()
cow = Cow()

# Store objects in a list
animals = [dog, cat, cow]

# Polymorphism through iteration
for animal in animals:
    animal.make_sound()


# The loop doesn't need to know whether the current object is a Dog, Cat, or Cow. It simply calls make_sound().
# Key concept: One interface, multiple object behaviors.