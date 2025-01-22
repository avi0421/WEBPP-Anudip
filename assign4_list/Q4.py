# Perform intersection operation on two lists

# Input two lists from the user
list1 = input("Enter elements of the first list separated by spaces: ").split()
list2 = input("Enter elements of the second list separated by spaces: ").split()

# Find the intersection
intersection = list(set(list1) & set(list2))

# Display the intersection
print("Intersection of the two lists:", intersection)
