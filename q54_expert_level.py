"""Question: Define a class TemplateMethod that uses the Template Method pattern
to define the skeleton of an algorithm.
Implement concrete classes that override specific steps of the algorithm.
"""


# Iris solution
class TemplateMethod:
    def execute(self):
        self.step1()
        self.step2()
        self.step3()

    def step1(self):
        raise NotImplementedError("Subclasses must implement this method")

    def step2(self):
        raise NotImplementedError("Subclasses must implement this method")

    def step3(self):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteClassA(TemplateMethod):
    def step1(self):
        print("ConcreteClassA: Step 1")

    def step2(self):
        print("ConcreteClassA: Step 2")

    def step3(self):
        print("ConcreteClassA: Step 3")

class ConcreteClassB(TemplateMethod):
    def step1(self):
        print("ConcreteClassB: Step 1")

    def step2(self):
        print("ConcreteClassB: Step 2")

    def step3(self):
        print("ConcreteClassB: Step 3")

# Use the Template Method pattern
objA = ConcreteClassA()
objA.execute()
# Output:
# ConcreteClassA: Step 1
# ConcreteClassA: Step 2
# ConcreteClassA: Step 3

objB = ConcreteClassB()
objB.execute()
# Output:
# ConcreteClassB: Step 1
# ConcreteClassB: Step 2
# ConcreteClassB: Step 3
