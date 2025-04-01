# Task 6: Work with Large Files
    # 1. Create a file named numbers.txt and write numbers from 1 to 1000, each on a new line.
    # 2. Write a Python program to:
    # Read the file.
    # Calculate and display the sum of all numbers in the file.

with open("numbers.txt", "w") as file:
    file.writelines(f"{i}\n" for i in range(1, 1001)) # looping from 1 till 1001 to get all numbers from 1 to 1000 and writing them in file 

with open("numbers.txt", "r") as file:
    total = sum(map(int, file)) # calculating total of each number in the file

#Printing the result
print("Sum of Numbers: ", total) 