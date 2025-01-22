# Question 1: Product and price dictionary

# Creating a dictionary to store products and their corresponding prices
product_prices = {
    "apple": 12,
    "banana": 10,
    "milk": 23,
    "bread": 10
}

# Printing the entire dictionary
print("Product Prices:", product_prices)

# Accessing the price of a specific product (e.g., apple)
print("Price of apple:", product_prices["apple"])

# Adding a new product
product_prices["orange"] = 15
print("Updated Product Prices:", product_prices)

# Updating the price of an existing product
product_prices["banana"] = 16
print("Updated Price of banana:", product_prices["banana"])

# Deleting a product from the dictionary
del product_prices["milk"]
print("Product Prices after deletion:", product_prices)
