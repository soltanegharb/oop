"""Question: Create a class Command that uses the Command pattern to
encapsulate a request as an object. Implement commands for TurnOn and TurnOff.
"""


# Iris solution
class Command:
    def execute(self):
        raise NotImplementedError("Subclasses must implement this method")

class TurnOn(Command):
    def execute(self):
        return "Turning on"

class TurnOff(Command):
    def execute(self):
        return "Turning off"

# Use the Command pattern
commands = [TurnOn(), TurnOff()]
for command in commands:
    print(command.execute())
