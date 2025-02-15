"""Question: Define a class named Book with attributes title, author, and pages.
Add a method to check if the book is a novel (more than 100 pages).
"""


# Iris solution
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_novel(self):
        return self.pages > 100

# Create an instance and check if it's a novel
book = Book("1984", "George Orwell", 328)
print(book.is_novel())  # Output: True
