# Task 7: Error Handling
    # 1. Write a Python program to handle the following scenarios:
    # Attempt to read a file named non_existent_file.txt and handle the FileNotFoundError.
    # Handle other potential exceptions that may arise during file operations.

# Trying to open a file that does not exist 
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e: # Handling the File Not Found exception 
    print("Error: File not found.", e)
except Exception as e: # Handling the Exception if it is not File Not Found exception
    print("An error occurred: ", e) 