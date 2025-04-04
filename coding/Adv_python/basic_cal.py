class BasicCalculator:
    def __init__(self):
        pass   
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

# Creating an object of the BasicCalculator class
calculator = BasicCalculator()

# Performing some calculations
print("Addition: ", calculator.add(10, 5))
print("Subtraction: ", calculator.subtract(10, 5))
print("Multiplication: ", calculator.multiply(10, 5))
print("Division: ", calculator.divide(10, 5))
