def find_maximum(num1, num2):
    return max(num1, num2)

# Input from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
maximum = find_maximum(a, b)
print(f"The maximum between {a} and {b} is {maximum}.")
