# Create a dynamic list and perform insert and delete operations

# Step 1: Get 5 elements from the user
my_list = []
for i in range(5):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

print("Initial List:", my_list)

# Step 2: Insert a new element
new_element = input("Enter a new element to insert: ")
position = int(input("Enter the position to insert the element (0-based index): "))
if 0 <= position <= len(my_list):
    my_list.insert(position, new_element)
    print("List after insertion:", my_list)
else:
    print("Invalid position!")

# Step 3: Delete an element
delete_element = input("Enter the element to delete: ")
if delete_element in my_list:
    my_list.remove(delete_element)
    print("List after deletion:", my_list)
else:
    print(f"Element '{delete_element}' not found in the list!")
