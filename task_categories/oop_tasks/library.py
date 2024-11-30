# TASK: Create a Library that can hold books.
"""
Create a class Book for idividual book data.
Create a class Library to hold multiple books.
    Console demo:
        Library:
        (empty)
        1. Add a book
        2. Delete a book
        3. Quit
        1
        Enter the book title: Test Book
        Enter the book author: Emanuel
        Enter the number of pages: 56
        Library:
        Book 1: Test Book by Emanuel, 56 pages
        1. Add a book
        2. Delete a book
        3. Quit
        2
        Enter a book name you want to delete: Test Book
        Library:
        (empty)
        1. Add a book
        2. Delete a book
        3. Quit
        3
        {exit the app}

Extra challenge: Don't use dictionaires.
"""


class Book():
    def __init__(self, title, author, num_pages) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages


class Library():
    def __init__(self) -> None:
        self.content = []

    def add_book(self, book):
        self.content.append(book)

    def delete_book(self, book_name):
        for book in self.content:
            if book.title == book_name:
                self.content.remove(book)
                return True
        return False

    def get_info(self):
        if not self.content:
            return "(empty)"
        info = ""
        for i, book in enumerate(self.content):
            info += f"Book {i + 1}: {book.title} by {book.author}, {book.num_pages} pages\n"
        return info.strip()


library = Library()

loop = True

while loop:
    print("Library:")
    print(library.get_info())
    print("1. Add a book")
    print("2. Delete a book")
    print("3. Quit")

    command = int(input())

    if command == 1:
        # add book
        title = input("Enter the book title: ")  # Test Book
        author = input("Enter the book author: ")  # Emanuel
        while True:
            try:
                num_pages = int(input("Enter the number of pages: "))  # 56
                break  # Exit the loop if successful conversion to int
            except ValueError:
                print("Invalid input. Please enter a valid  number of pages.")
        library.add_book(Book(title, author, num_pages))

    elif command == 2:
        # delete book
        title = input("Enter the book name you want to delete: ")  # Test Book
        if not library.delete_book(title):
            print(f"Book '{title}' not found in the library.")

    elif command == 3:
        # quit
        loop = False

    else:
        print("No valid command")


# Entering a string as a number of pages breaks the app (FIXED)
