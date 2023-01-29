"""
Task 1#

Implement properties as instance variables, and set them to None or 0.

Account has the following properties:

    title
    balance

SavingsAccount has the following properties:

    interestRate


Task 2#

Create an initializer for Account class. The order of parameters should be the following, where Mark is the title, and
5000 is the account balance:

Account("Mark",5000)

Task 3#

Implement properties as instance variables, and set them to None or 0.

Create an initializer for the SavingsAccount class using the initializer of the Account class in the order below:

Account("Mark",5000,5)

Task 4#

In the Account class, implement the getBalance() method that returns balance.

Task 5#

In the Account class, implement the deposit(amount) method that adds amount to the balance. It does not return anything.

Task 6#

In the Account class, implement the withdrawal(amount) method that subtracts the amount from the balance. It does not
return anything.

Task 7#

In the SavingsAccount class, implement an interestAmount() method that returns the interest amount of the current
balance. Below is the formula for calculating the interest amount:
"""


class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interest_rate=0):
        super().__init__(title, balance)
        self. interest_rate = interest_rate

    def interest_amount(self):
        return (self.interest_rate * self.balance) * 100


new_account = SavingsAccount("Steve", 5000, 10)
print("Initial Balance:", new_account.get_balance())
new_account.withdraw(1000)
print("Balance after withdrawal:", new_account.get_balance())
new_account.deposit(500)
print("Balance after deposit:", new_account.get_balance())
print("Interest on current balance:", new_account.interest_amount())
