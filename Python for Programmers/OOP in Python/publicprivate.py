class Employee:
    def __init__(self, ID, salary):
        # id is public
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary) # it will be able to reveal salary

    def displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
Steve.displaySalary()
# you can still access a private property if the user uses _<ClassName> prefix for property or method
print(Steve._Employee__salary)
