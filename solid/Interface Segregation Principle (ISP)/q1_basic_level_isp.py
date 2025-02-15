"""Question: Define an interface Printer with methods print_document and scan_document.
Create classes BasicPrinter and AllInOnePrinter that implement the interface.
Refactor the interface to adhere to the Interface Segregation Principle.
"""


# Iris solution
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

    @abstractmethod
    def scan_document(self, document):
        pass

class BasicPrinter(Printer):
    def print_document(self, document):
        return f"Printing: {document}"

    def scan_document(self, document):
        raise NotImplementedError("BasicPrinter cannot scan documents")

class AllInOnePrinter(Printer):
    def print_document(self, document):
        return f"Printing: {document}"

    def scan_document(self, document):
        return f"Scanning: {document}"

# Refactored interfaces adhering to ISP
class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class BasicPrinter(Printer):
    def print_document(self, document):
        return f"Printing: {document}"

class AllInOnePrinter(Printer, Scanner):
    def print_document(self, document):
        return f"Printing: {document}"

    def scan_document(self, document):
        return f"Scanning: {document}"

# Usage
basic_printer = BasicPrinter()
all_in_one_printer = AllInOnePrinter()
print(basic_printer.print_document("Document1"))
print(all_in_one_printer.print_document("Document2"))
print(all_in_one_printer.scan_document("Document2"))
