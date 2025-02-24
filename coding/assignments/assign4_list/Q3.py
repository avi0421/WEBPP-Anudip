# Find the second smallest element in a list

# Input the list from the user
my_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

if len(my_list) < 2:
    print("List must have at least two elements!")
else:
    my_list.sort()  # Sort the list
    # Find the second smallest element
    second_smallest = None
    for num in my_list:
        if num > my_list[0]:  # Find the first number greater than the smallest
            second_smallest = num
            break

    if second_smallest is None:
        print("No second smallest element exists!")
    else:
        print("Second Smallest Element:", second_smallest)
