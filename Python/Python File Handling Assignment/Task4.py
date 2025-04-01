# Task 4: Analyze the File
    # 1. Write a Python program to count and display:
    # The total number of students in the file.
    # The number of students who received a grade 'A'.

with open("students.txt", "r") as file:
    lines = file.readlines()

# Calculating total no of students
total_students = len(lines) - 1

# Calculating the number of students having grade 'A'
grade_a_count = sum(1 for line in lines[1:] if line.strip().split(",")[2].strip() == 'A')

#Printing the results
print("Total Students: ", total_students)
print("Students with Grade A: ", grade_a_count)