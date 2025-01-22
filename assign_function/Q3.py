def can_vote(age):
    return age >= 18

# Input from the user
age = int(input("Enter the age of the person: "))
if can_vote(age):
    print("The person is eligible to vote.")
else:
    print("The person is not eligible to vote.")
