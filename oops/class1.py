class Person:
    def __init__(self, name, age):  # Corrected the method signature and indentation
        self.name = name  # Corrected the assignment (used '=' instead of '-')
        self.age = age  # Corrected the assignment (used '=' instead of '-')

    def display(self):
        print("The person is", self.name)

# Creating objects of Person class
admin = Person("Ramanand", 56)  # Corrected variable name and instantiation
admin.display()

accountant = Person("Karishma", 25)  # Corrected variable name and instantiation
accountant.display()

print(admin.name)  # Corrected to print the 'name' attribute of the admin object

'''

OOPS is a way of organizing code that uses objects and classes to represent 
real-world entities and their behavior. In OOPs, object has attributes thing 
that has specific data and can perform certain actions using methods.

OOPS Concepts in Python
> Class in Python
> Objects in Python
> Polymorphism in Python
> Encapsulation in Python
> Inheritance in Python
> Data Abstraction in Python

Creating a Class
Here, the class keyword indicates that we are creating a 
class followed by name of the class (Car in this case).
class Car:
    def __init__(self, brand, model):  # Constructor
        self.brand = brand
        self.model = model

# Creating objects of Car class
my_car = Car("Toyota", "Corolla")  # Constructor is called automatically
my_car1 = Car("Hyundai", "i10")
my_car3 = Car("Honda", "HondaCity")

# Accessing and printing brand of the car
print(my_car.brand)  # Output: Toyota

'''

'''
# Accessing brand of the car
print(my_car.brand)  # Output: Toyota

# Q.2) Explanation of the __init__ method in Python
# __init__ is a special method (constructor) used to initialize an object's attributes when it is created.

class Person:
    def __init__(self, name, age):  # Constructor method to initialize attributes
        self.name = name
        self.age = age

# Creating an object of Person class
person = Person("Alice", 30)

# Accessing and printing the name attribute of the person object
print(person.name)  # Output: Alice

'''