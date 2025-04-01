# Task 9: Copy File Content
    # 1. Write a Python program to copy the content of students.txt into a new file named
    # students_backup.txt.

# Copying the content from 'students.txt' file and pasting it in the 'students_backup.txt' file
with open("students.txt") as source, open("students_backup.txt", "w") as dest: 
    for line in source:
        dest.write(line)