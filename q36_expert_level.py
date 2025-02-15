"""Question: Implement a class ThreadSafeSingleton using threading to ensure
thread-safe singleton behavior.
"""


# Iris solution
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(ThreadSafeSingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Demonstrate thread-safe singleton behavior
def create_singleton():
    singleton = ThreadSafeSingleton()
    print(singleton)

threads = [threading.Thread(target=create_singleton) for _ in range(5)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
