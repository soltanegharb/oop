"""Question: Define a class Mediator that uses the Mediator pattern to coordinate
interactions between multiple objects.
Implement colleagues ColleagueA and ColleagueB that communicate through the mediator.
"""


# Iris solution
class Mediator:
    def notify(self, sender, event):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteMediator(Mediator):
    def __init__(self):
        self._colleague_a = None
        self._colleague_b = None

    def set_colleague_a(self, colleague):
        self._colleague_a = colleague

    def set_colleague_b(self, colleague):
        self._colleague_b = colleague

    def notify(self, sender, event):
        if event == "A":
            print("Mediator reacts on A and triggers B")
            self._colleague_b.do_b()
        elif event == "B":
            print("Mediator reacts on B and triggers A")
            self._colleague_a.do_a()

class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator

class ColleagueA(Colleague):
    def do_a(self):
        print("ColleagueA does A")
        self._mediator.notify(self, "A")

class ColleagueB(Colleague):
    def do_b(self):
        print("ColleagueB does B")
        self._mediator.notify(self, "B")

# Use the Mediator pattern
mediator = ConcreteMediator()
colleague_a = ColleagueA(mediator)
colleague_b = ColleagueB(mediator)
mediator.set_colleague_a(colleague_a)
mediator.set_colleague_b(colleague_b)

colleague_a.do_a()
# Output:
# ColleagueA does A
# Mediator reacts on A and triggers B
# ColleagueB does B
