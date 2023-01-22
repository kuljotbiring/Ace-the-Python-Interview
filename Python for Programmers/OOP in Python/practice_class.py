class Employee:

    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


# create an object from the class and set its properties
Kuljot = Employee(1000305967, 675000, "Software")

print(f"Kuljot: ID: {Kuljot.ID}, Salary: {Kuljot.salary}, Department: {Kuljot.department}")


