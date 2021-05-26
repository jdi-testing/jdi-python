import os


class User:
    @staticmethod
    def default():
        return User()

    def __init__(self):
        self.login = "epam"
        self.password = os.getenv("TEST_PASSWORD")
        self.name = "Name"
        self.last_name = "Last Name"
        self.description = "Description"
