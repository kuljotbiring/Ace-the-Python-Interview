"""
Implement the basic structure of a parent class, Account, and a child class, SavingsAccount.
Task 1
Implement properties as instance variables, and set them to None or 0.

Account has the following properties:
    title
    balance

SavingsAccount has the following properties:
    interestRate

Task 2
Create an initializer for Account class. The order of parameters should be the following, where Mark is the title, and
5000 is the account balance:

Account("Mark", 5000)

Task 3
Implement properties as instance variables, and set them to None or 0.

Create an initializer for the SavingsAccount class using the initializer of the Account class in the order below:

Account("Mark", 5000, 5)

Here, Mark is the title and 5000 is the balance and 5 is the interestRate.

In the Account class, implement the getBalance() method that returns balance.

Task 4
In the Account class, implement the deposit(amount) method that adds amount to the balance. It does not return anything.

Sample input

balance = 2000
deposit(500)
getbalance()

Sample output

2500

Task 5
In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance. It does not
return anything.

Sample input

balance = 2000
withdrawal(500)
getbalance()

Sample output

1500

Task 6
In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current
balance. Below is the formula for calculating the interest amount:

Sample input

balance = 2000
interestRate = 5
interestAmount()

Sample output

100
"""


class Account:
    def __init__(self, title=None, balance=0):
        # write your code here
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        # write code here
        self.balance -= amount

    def deposit(self, amount):
        # write code here
        self.balance += amount

    def getBalance(self):
        # write code here
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        # write code here
        return (self.interestRate * self.balance) / 100


# code to test - do not edit this
demo1 = SavingsAccount("Mark", 2000, 5)  # initializing a SavingsAccount object
