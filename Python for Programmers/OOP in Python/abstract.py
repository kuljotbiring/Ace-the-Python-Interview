"""
Abstract base classes define a set of methods and properties that a class must implement in order to be considered a
duck-type instance of that class.

To define an abstract base class, we use the abc module. The abstract base class is inherited from the built-in ABC
class. We have to use the decorator @abstractmethod above the method that we want to declare as an abstract method.
"""


from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 4 * self.length


square = Square(4)
# this code will not generate an error since abastract methods have been
# defined in the child class, Square