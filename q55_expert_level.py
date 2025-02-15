"""Question: Implement a class Visitor that uses the Visitor pattern to perform
operations on elements of an object structure.
Define elements ElementA and ElementB that accept visitors.
"""


# Iris solution
class Visitor:
    def visit_element_a(self, element):
        raise NotImplementedError("Subclasses must implement this method")

    def visit_element_b(self, element):
        raise NotImplementedError("Subclasses must implement this method")

class Element:
    def accept(self, visitor):
        raise NotImplementedError("Subclasses must implement this method")

class ElementA(Element):
    def accept(self, visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    def accept(self, visitor):
        visitor.visit_element_b(self)

class ConcreteVisitor(Visitor):
    def visit_element_a(self, element):
        print("Visiting ElementA")

    def visit_element_b(self, element):
        print("Visiting ElementB")

# Use the Visitor pattern
elements = [ElementA(), ElementB()]
visitor = ConcreteVisitor()
for element in elements:
    element.accept(visitor)
# Output:
# Visiting ElementA
# Visiting ElementB
