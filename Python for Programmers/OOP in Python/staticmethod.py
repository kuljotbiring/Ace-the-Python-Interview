"""
Static methods do not know anything about the state of the class, i.e., they cannot modify class attributes. The purpose
of a static method is to use its parameters and produce a useful result.
"""


class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))
