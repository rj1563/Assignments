# Task 2: Read the File
    # 1. Write a Python program to read the students.txt file and display its content on the console.
    # 2. Split the content line by line and print each line separately.

with open("students.txt", "r") as file:  #reading the data from students.txt
    content = file.read()  # Storing the data of the file in 'content'
    print("File content: ", content)

    lines = content.splitlines() #Spliting the data from 'content'
    print("\nLines: ")
    for line in lines:
        print(line)