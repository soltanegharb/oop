"""Question: Define a class named Library with attributes name and books
(a list of book titles). Add methods to add a book, remove a book, and list all books.
"""


from typing import List










# My solution
class Library:
    def __init__(self, name:str, books:List[str]):
        self.name = name
        self.books = books
    
    def add_book(self, book_title:str):
        self.books.append(book_title)
    
    def remove_book(self, book_title:str):
        try:
            finded_book_index = self.books.index(book_title)
        except ValueError('book not in books'):
            pass

    def list_books(self):
        return self.books


allame_rafiei_library = Library(name='allame_rafiei', books=['quran', 'riazi', 'physics'])
print(allame_rafiei_library.books)
allame_rafiei_library.add_book('tarikh')
print(allame_rafiei_library.list_books())
allame_rafiei_library.remove_book('tarikh')
print(allame_rafiei_library.list_books())


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
