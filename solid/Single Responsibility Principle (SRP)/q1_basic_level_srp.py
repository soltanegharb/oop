"""Question: Define a class User that has methods to get and set user information.
Refactor the class to adhere to the Single Responsibility Principle
by separating user information management from user authentication.
"""


# Iris solution
# Initial class violating SRP
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_user_info(self):
        return {"username": self.username, "password": self.password}

    def authenticate(self, password):
        return self.password == password

# Refactored classes adhering to SRP
class UserInfo:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_user_info(self):
        return {"username": self.username, "password": self.password}

class UserAuth:
    def __init__(self, user_info):
        self.user_info = user_info

    def authenticate(self, password):
        return self.user_info.password == password

# Usage
user_info = UserInfo("john_doe", "securepassword")
user_auth = UserAuth(user_info)
print(user_auth.authenticate("securepassword"))  # Output: True
