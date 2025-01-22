# Basic Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

# Create a calculator object
calc = Calculator()

# Perform operations
print(calc.add(10, 5))      # Output: 15
print(calc.subtract(10, 5)) # Output: 5
print(calc.multiply(10, 5)) # Output: 50
print(calc.divide(10, 5))   # Output: 2.0
