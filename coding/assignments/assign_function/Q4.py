def print_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

# Input from the user
number = int(input("Enter a number to get its multiplication table: "))
print_table(number)
