"""Question: Create a class Observable that allows observers to subscribe
and get notified when the state changes.
Implement the observer pattern using private and protected attributes.
"""










# Iris solution
class Observable:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received message: {message}")

# Create observable and observers
observable = Observable()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

# Subscribe observers
observable.subscribe(observer1)
observable.subscribe(observer2)

# Notify observers
observable.notify("State has changed")
