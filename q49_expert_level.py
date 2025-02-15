"""Question: Implement a class Proxy that uses the Proxy pattern to control
access to another object.
"""


# Iris solution
class RealSubject:
    def request(self):
        return "RealSubject: Handling request."

class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            return self._real_subject.request()
        else:
            return "Proxy: Access denied."

    def check_access(self):
        # Simulate access control
        return True

# Use the Proxy pattern
real_subject = RealSubject()
proxy = Proxy(real_subject)
print(proxy.request())  # Output: RealSubject: Handling request.
