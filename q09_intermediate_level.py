"""Question: Define a class named Library with attributes name and books
(a list of book titles). Add methods to add a book, remove a book, and list all books.
"""


# Iris solution
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book_title):
        self.books.append(book_title)

    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)

    def list_books(self):
        return self.books

# Create an instance and perform operations
library = Library("City Library")
library.add_book("1984")
library.add_book("To Kill a Mockingbird")
library.remove_book("1984")
print(library.list_books())  # Output: ['To Kill a Mockingbird']
