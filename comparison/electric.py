units = float(input("Enter the number of units consumed: "))

bill = 0

if units > 0 and units <= 100:
    bill = units * 10
elif units <= 200:
    bill = 1000 + (units - 100) * 15
elif units <= 300:
    bill = 1000 + 1500 + (units - 200) * 20
elif units > 300:
    bill = 1000 + 1500 + 2000 + (units - 300) * 25
else:
    print("Invalid input. Please enter a number greater than 0.")
    bill = None

if bill is not None:
    print(f"The total bill for {units} units is: Rs {bill:.2f}")
