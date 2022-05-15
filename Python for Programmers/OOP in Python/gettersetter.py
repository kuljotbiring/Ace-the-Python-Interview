class User:
    def __init__(self, username=None):  # defining initializer
        self.__username = username

    def set_username(self, x):
        self.__username = x

    def get_username(self):
        return self.__username


Steve = User('steve1')
print('Before setting:', Steve.get_username())
Steve.set_username('steve2')
print('After setting:', Steve.get_username())
