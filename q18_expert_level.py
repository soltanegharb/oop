"""Question: Create a class Observable that allows observers to subscribe
 and get notified when the state changes. Implement the observer pattern.
"""










# Iris solution
class Observer:
    def update(self, state):
        pass

class Observable:
    def __init__(self):
        self._observers = []
        self._state = None

    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._state)

    def set_state(self, state):
        self._state = state
        self.notify_observers()

    def get_state(self):
        return self._state

class ConcreteObserver(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, state):
        print(f"{self._name} received state change: {state}")


observable = Observable()

observer1 = ConcreteObserver("Observer 1")
observer2 = ConcreteObserver("Observer 2")

observable.subscribe(observer1)
observable.subscribe(observer2)

observable.set_state("State 1")
observable.set_state("State 2")

observable.unsubscribe(observer1)
observable.set_state("State 3")
