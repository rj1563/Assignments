# Task 8: Real-World Application
    # 1. Create a class Library with attributes:
    # books (list of book titles)
    # 2. Add methods to:
    # Display all books in the library.
    # Borrow a book (remove it from the list).
    # Return a book (add it back to the list).
    # 3. Write a program to:
    # Create a Library object with an initial list of books.
    # Allow the user to interact with the library through a menu-driven program:
    # Display books
    # Borrow a book
    # Return a book
    # exit

# Main class
class Library:

    # Constructor for initializing the data member
    def __init__(self, books):
        self.books = books
    
    # Method to display all the books in the library
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books:")
            for book in self.books:
                print(f"- {book}")
    
    # Method to borrow a book from the library
    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"You borrowed '{book}'.")
        else:
            print(f"'{book}' is not available in the library.")
    
    # Method to return a book from the library
    def return_book(self, book):
        if book in self.books:
            print(f"'{book}' is already in the library. No need to return it.")
        else:
            self.books.append(book)
            print(f"Thank you for returning '{book}'.")

# Initialize Library object
library = Library(["Database Design", "SQL Queries", "Python Programming"])

while True:
    print("\n1. Display Books\n2. Borrow Book\n3. Return Book\n4. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        library.display_books()
    elif choice == 2:
        book = input("Enter the book name to borrow: ").strip()
        library.borrow_book(book)
    elif choice == 3:
        book = input("Enter the book name to return: ").strip()
        library.return_book(book)
    elif choice == 4:
        print("Exiting the program. Thank you for using the library!")
        break
    else:
        print("Invalid choice! Please select a valid option.")