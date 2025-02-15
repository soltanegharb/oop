"""Question: Create a class Database with methods connect and disconnect.
Implement a class Application that depends on Database.
Refactor the classes to adhere to
the Dependency Inversion Principle by introducing an interface DatabaseConnection.
"""


# Iris solution
# Initial classes violating DIP
class Database:
    def connect(self):
        return "Database connected"

    def disconnect(self):
        return "Database disconnected"

class Application:
    def __init__(self, database):
        self.database = database

    def start(self):
        return self.database.connect()

    def stop(self):
        return self.database.disconnect()

# Refactored classes adhering to DIP
from abc import ABC, abstractmethod

class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class Database(DatabaseConnection):
    def connect(self):
        return "Database connected"

    def disconnect(self):
        return "Database disconnected"

class Application:
    def __init__(self, database: DatabaseConnection):
        self.database = database

    def start(self):
        return self.database.connect()

    def stop(self):
        return self.database.disconnect()

# Usage
database = Database()
app = Application(database)
print(app.start())  # Output: Database connected
print(app.stop())   # Output: Database disconnected
