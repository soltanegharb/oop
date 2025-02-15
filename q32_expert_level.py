"""Question: Create a class Document with a class attribute document_count 
to keep track of the number of documents created.
Add methods to read and write content to the document.
Use class methods to get the document count.
"""


# Iris solution
class Document:
    document_count = 0

    def __init__(self, title, content=""):
        self.title = title
        self.content = content
        Document.document_count += 1

    def read(self):
        return self.content

    def write(self, content):
        self.content = content

    @classmethod
    def get_document_count(cls):
        return cls.document_count

# Create instances and perform operations
doc1 = Document("Doc1", "Content of Doc1")
doc2 = Document("Doc2", "Content of Doc2")
print(Document.get_document_count())  # Output: 2
