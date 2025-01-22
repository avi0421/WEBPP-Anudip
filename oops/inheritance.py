# Base class
class Animal:
    def speak(self):
        print("Animal Speaking")

# Child class Dog inherits from the Animal class
class Dog(Animal):
    def bark(self):
        print("Dog barking")

# Creating an object of Dog class
d = Dog()

# Calling methods from Dog and Animal classes
d.bark()  # Output: Dog barking
d.speak()  # Output: Animal Speaking
