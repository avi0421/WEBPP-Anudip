# Task Q1: Employee Names in Sales Department in Uppercase
employees = [
    {"name": "John Doe", "department": "Sales", "salary": 50000},
    {"name": "Jane Smith", "department": "Marketing", "salary": 60000},
    {"name": "Alice Johnson", "department": "Sales", "salary": 55000},
    {"name": "Bob Brown", "department": "HR", "salary": 40000}
]

# List comprehension to filter Sales department employees and convert their names to uppercase
sales_employees = [employee["name"].upper() for employee in employees if employee["department"] == "Sales"]

# Print the result
print(sales_employees)

# Task Q2: Extract domain part from email addresses
emails = [
    "john.doe@example.com",
    "jane.smith@company.org",
    "alice.johnson@domain.net"
]

# List comprehension to extract domain part from each email
domains = [email.split('@')[1] for email in emails]

# Print the result
print(domains)

# Task Q3: Filter URLs that start with 'https'
urls = [
    "http://example.com",
    "https://secure-site.com",
    "ftp://files.example.org",
    "https://another-secure-site.com"
]

# List comprehension to filter URLs starting with 'https'
https_urls = [url for url in urls if url.startswith('https')]

# Print the result
print(https_urls)
