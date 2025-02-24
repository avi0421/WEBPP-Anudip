# Question 3: Customer ID and name dictionary

# Creating a dictionary to store customer IDs and their names
customer_info = {
    1: "A",
    2: "B",
    3: "C",
    4: "D"
}

# Printing the entire dictionary
print("Customer Information:", customer_info)

# Accessing the name of a specific customer ID (e.g., 2)
print("Customer with ID 2:", customer_info[2])

# Adding a new customer ID and name
customer_info[5] = "E"
print("Updated Customer Information:", customer_info)

# Updating the name of an existing customer
customer_info[1] = "A"
print("Updated Customer with ID 1:", customer_info[1])

# Deleting a customer from the dictionary
del customer_info[3]
print("Customer Information after deletion:", customer_info)
