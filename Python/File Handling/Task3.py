# Task 3: Append Data to the File
    # 1. Add the following data to the students.txt file:
    # Emma, 20, B
    # Liam, 23, A
    # 2. Ensure that the new data is appended without overwriting the existing content.

with open("students.txt", "a") as file:
    file.write("Emma, 20, B\n")
    file.write("Liam, 23, A\n")