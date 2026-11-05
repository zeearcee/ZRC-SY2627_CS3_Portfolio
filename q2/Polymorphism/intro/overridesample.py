class Animal:
    def make_sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def make_sound(self):
        print("Dog says Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Cat says Meow!")


# Creating objects
dog = Dog()
cat = Cat()

# Calling overridden methods
dog.make_sound()
cat.make_sound()