# Task 5: Update the File
    # 1. Write a Python program to update the age of 'Sophie' to 23 in the students.txt file.
    # 2. Save the updated data back to the file

with open("students.txt", "r") as file:
    lines = file.readlines()

with open("students.txt", "w") as file:
    for line in lines:
        if line.startswith("Sophie"):
            line = "Sophie, 23, C\n"
        file.write(line)