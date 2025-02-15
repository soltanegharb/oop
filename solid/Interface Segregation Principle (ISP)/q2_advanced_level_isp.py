"""Question: Create an interface Worker with methods work and eat.
Implement classes HumanWorker and RobotWorker that adhere to
the Interface Segregation Principle.
"""


# Iris solution
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"

class RobotWorker(Worker):
    def work(self):
        return "Robot is working"

    def eat(self):
        raise NotImplementedError("Robot does not eat")

# Refactored interfaces adhering to ISP
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(Worker, Eater):
    def work(self):
        return "Human is working"

    def eat(self):
        return "Human is eating"

class RobotWorker(Worker):
    def work(self):
        return "Robot is working"

# Usage
human_worker = HumanWorker()
robot_worker = RobotWorker()
print(human_worker.work())
print(human_worker.eat())
print(robot_worker.work())
