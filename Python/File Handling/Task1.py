# Task 1: Create a File
    # 1. Write a Python program to create a file named students.txt.
    # 2. Write the following data into the file:
    # Name, Age, Grade
    # John, 20, A
    # Alice, 19, B
    # Mark, 21, A
    # Sophie, 22, C

with open("students.txt", "w") as file:  # creating a file named students.txt and writing the data in the file
    file.write("Name, Age, Grade\n")
    file.write("John, 20, A\n")
    file.write("Alice, 19, B\n")
    file.write("Mark, 21, A\n")
    file.write("Sophie, 22, C\n")