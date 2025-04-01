# Task 8: Word Count
    # 1. Create a file named paragraph.txt and add a paragraph of your choice.
    # 2. Write a Python program to:
    # Count the total number of words in the file.
    # Count the occurrences of a specific word entered by the user.

# Creating the file
with open("paragraph.txt", "w") as file:
    file.write("This is a sample paragraph. This paragraph is for testing purpose.")

# Reading the file
with open("paragraph.txt", "r") as file:
    content = file.read() # Storing the content of file
    words = content.split() # Splitting each word 
    word_count = len(words) # Calculating the total number of words

    user_input = input("Enter a word to count its occurrences: ").strip()
    word_occurence = words.count(user_input)

# Printing the result
print("Total number of words: ", word_count)
print(f"Occurrences of '{user_input}':", word_occurence)