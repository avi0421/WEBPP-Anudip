
products = {
    "apple": 50,
    "banana": 30,
    "yoghurt": 80,
    "milk": 25,
    "bread": 20
}
print(products)

# price of product
x = products['milk']
print("The price of milk is Rs.", x)

# Getting price
x = products.get("banana")
print("The price of banana is Rs.", x)

# find all keys present in dictionary
y = products.keys()
print("The keys present are:", y)

# To update dictionary element
products.update({"yoghurt": 90})
print(products)

# To add new element in dictionary
products["paneer"] = 70
print(products)

products["grade"]

# Removing the last added product from the dictionary
products.popitem()  # removes the last added item (cheese)
print("After removing the last item:")
print(products)

# Looping over the dictionary
print("Looping over products:")
for i in products:
    print(i)

# Getting keys from the dictionary
print("Getting product keys:")
for i in products.keys():
    print(i)

# Getting values from the dictionary
print("Getting product prices:")
for i in products.values():
    print(i)

# Getting items (keys & values) from the dictionary
print("Getting products and their prices:")
for x, y in products.items():
    print(x, y)
