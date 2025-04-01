# Task 10: Delete a File
    # 1. Write a Python program to delete the file students_backup.txt 
    # after confirming from the user.

import os

if os.path.exists("students_backup.txt"): # if the 'students_backup.txt' file exist
    confirm = input("Do you want to delete students_backup.txt? (yes/no): ").strip().lower() # Asking the user if they want to delete the file or not
    if confirm == "yes": # if user enters 'yes' then delete the file
        os.remove("students_backup.txt")
        print("File deleted.")
    else:
        print("File not deleted.") # if user enters 'no' then don't delete the file
else:
    print("File does not exist.") # if the file does not exist