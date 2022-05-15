"""
Implement the complete Student class by completing the tasks below
Task#

Implement the following properties as private:

    name
    rollNumber

Include the following methods to get and set the private properties above:

    getName()
    setName()
    getRollNumber()
    setRollNumber()

Implement this class according to the rules of encapsulation.
Input

Checking all the properties and methods
Output

Expecting perfectly defined fields and getter/setters

    Note: Do not use initializers to initialize the properties. Use the set methods to do so. If the setter is not
    defined properly, the corresponding getter will also generate an error even if the getter is defined properly.

"""


class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, roll_number):
        self.__rollNumber = roll_number


student = Student()
student.setName("Kuljot")
student.setRollNumber(100)

print(f"Printing Name: {student.getName()}")
print(f"Printing RollNumber: {student.getRollNumber()}")
