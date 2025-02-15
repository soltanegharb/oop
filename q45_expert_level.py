"""Question: Define a class Event that uses the observer pattern to notify
multiple listeners when an event occurs. Implement methods to add and remove listeners.
"""


# Iris solution
class Event:
    def __init__(self):
        self._listeners = []

    def add_listener(self, listener):
        self._listeners.append(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

    def notify(self, *args, **kwargs):
        for listener in self._listeners:
            listener(*args, **kwargs)

# Create an event and listeners
def listener1(event_data):
    print(f"Listener 1 received: {event_data}")

def listener2(event_data):
    print(f"Listener 2 received: {event_data}")

event = Event()
event.add_listener(listener1)
event.add_listener(listener2)

# Notify listeners
event.notify("Event occurred")  # Output: Listener 1 received: Event occurred \n Listener 2 received: Event occurred
