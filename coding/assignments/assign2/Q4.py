# program to calculate the total salary including DA and HRA if the basic salary is more than 50000.

# Input basic salary from user
basic_salary = float(input("Enter the basic salary: "))

# Calculate DA and HRA if salary is more than 50000
if basic_salary > 50000:
    da = 0.10 * basic_salary  # For 10% DA we use 0.10
    hra = 0.12 * basic_salary # For 12% HRA we use 0.12
else:
    da = 0  
    hra = 0

# Calculate total salary
total_salary = basic_salary + da + hra

# Display the total salary
print("The total salary is:", total_salary)
