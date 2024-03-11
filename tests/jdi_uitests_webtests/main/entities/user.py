import os


class User:
    @staticmethod
    def default():
        return User()

    def __init__(self):
        self.login = "Roman"
        self.password = "Jdi1234"
