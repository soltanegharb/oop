"""Question: Create a class Publisher that allows subscribers to subscribe
and get notified when a new article is published. Implement the observer pattern.
"""










# Iris solution
class Publisher:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def publish(self, article):
        for subscriber in self._subscribers:
            subscriber.notify(article)

class Subscriber:
    def notify(self, article):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteSubscriber(Subscriber):
    def notify(self, article):
        print(f"New article published: {article}")

# Create publisher and subscribers
publisher = Publisher()
subscriber1 = ConcreteSubscriber()
subscriber2 = ConcreteSubscriber()

# Subscribe to publisher
publisher.subscribe(subscriber1)
publisher.subscribe(subscriber2)

# Publish an article
publisher.publish("Understanding the Observer Pattern")
