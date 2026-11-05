# Polymorphism is one of the four fundamental principles of Object-Oriented Programming (OOP). It means "many forms." It allows different objects to use the same method name but perform different behaviors depending on the object.


class Dog:
    def make_sound(self):
        print("Dog: Woof! Woof!")


class Cat:
    def make_sound(self):
        print("Cat: Meow! Meow!")


class Cow:
    def make_sound(self):
        print("Cow: Moo! Moo!")


# Object creation
dog = Dog()
cat = Cat()
cow = Cow()

# Same method, different behaviors
dog.make_sound()
cat.make_sound()
cow.make_sound()



# All three classes have the same method name: make_sound().
# Each class implements the method differently.
# The same method call produces different outputs.