# Q1: Create a list of names of employees who work in the 'Sales' department, all in uppercase.

# List of employee records
employees = [
    {"name": "Alice", "department": "Sales", "salary": 50000},
    {"name": "Bob", "department": "HR", "salary": 45000},
    {"name": "Charlie", "department": "Sales", "salary": 55000},
    {"name": "David", "department": "IT", "salary": 60000}
]

# Create a list of names of employees in the Sales department, in uppercase
sales_employees = [emp['name'].upper() for emp in employees if emp['department'] == 'Sales']

# Print the result
print(sales_employees)
