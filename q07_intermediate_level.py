"""Question: Define a class named Book with attributes title, author, and pages.
Add a method to check if the book is a novel (more than 100 pages).
"""










# My solution
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_novel(self):
        if self.pages > 100:
            return True
        else:
            return False


riazi_panjom_dabestan = Book(title='riazi panjom', author='Soltani', pages=190)
tarfand_haye_riazi = Book(title='tarfand haye riazi', author='Soltani', pages=50)
print(riazi_panjom_dabestan.is_novel())


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
