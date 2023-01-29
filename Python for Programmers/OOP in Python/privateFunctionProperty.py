class Employee:
    def __init__(self, id_num, salary):
        self.id_num = id_num
        self.__salary = salary  # salary is a private property

    def display_salary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __display_id(self):  # displayID is a private method
        print("ID:", self.id_num)


Steve = Employee(3789, 2500)
Steve.displaySalary()
Steve.__displayID()  # this will generate an error
print(Steve._Employee__salary)  # accessing a private property
