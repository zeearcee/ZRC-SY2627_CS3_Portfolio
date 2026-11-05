class Animal:
    def make_sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def make_sound(self):
        print("Dog says Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Cat says Meow!")


class Cow(Animal):
    def make_sound(self):
        print("Cow says Moo!")


# Creating objects
animals = [Dog(), Cat(), Cow()]

# Polymorphism
for animal in animals:
    animal.make_sound()

