"""Question: Create a class ThreadSafeCounter that uses threading to ensure
thread-safe increment and decrement operations.
"""


# Iris solution
import threading

class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += 1

    def decrement(self):
        with self._lock:
            self.value -= 1

    def get_value(self):
        with self._lock:
            return self.value

# Demonstrate thread-safe counter
counter = ThreadSafeCounter()

def increment_counter():
    for _ in range(1000):
        counter.increment()

threads = [threading.Thread(target=increment_counter) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(counter.get_value())  # Output: 10000
