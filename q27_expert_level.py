"""Question: Create a class Logger with a private class attribute _instance
to implement the Singleton pattern.
Ensure that only one instance of the class can be created.
"""










# Iris solution
class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def log(self, message):
        print(f"Log: {message}")

# Demonstrate Singleton pattern
logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)  # Output: True
logger1.log("This is a log message.")
