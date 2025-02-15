"""Question: Create a class ChainOfResponsibility that uses the Chain of Responsibility
pattern to pass a request along a chain of handlers.
Implement handlers HandlerA and HandlerB.
"""


# Iris solution
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            self._successor.handle(request)

class HandlerA(Handler):
    def handle(self, request):
        if request == "A":
            print("HandlerA handled request")
        else:
            super().handle(request)

class HandlerB(Handler):
    def handle(self, request):
        if request == "B":
            print("HandlerB handled request")
        else:
            super().handle(request)

# Use the Chain of Responsibility pattern
handler_chain = HandlerA(HandlerB())
handler_chain.handle("A")  # Output: HandlerA handled request
handler_chain.handle("B")  # Output: HandlerB handled request
handler_chain.handle("C")  # No output
