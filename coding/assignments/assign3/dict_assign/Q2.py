# Question 2: Student and grade dictionary

# Creating a dictionary to store students and their grades
student_grades = {
    "Jay": "A",
    "Vijay": "B",
    "Ajay": "A",
    "Simba": "C"
}

# Printing the entire dictionary
print("Student Grades:", student_grades)

# Accessing the grade of a specific student (e.g., Jay)
print("Grade of Jay:", student_grades["Jay"])

# Adding a new student and their grade
student_grades["Hetal"] = "B"
print("Updated Student Grades:", student_grades)

# Updating the grade of an existing student
student_grades["VIjay"] = "B"
print("Updated Grade of Vijay:", student_grades["Vijay"])

# Deleting a student from the dictionary
del student_grades["Simba"]
print("Student Grades after deletion:", student_grades)
