"""
n this challenge, you must implement the factorial() function. It takes an integer as a parameter and calculates its
factorial. Python does have a built-in factorial function but you’ll be creating your own for practice.

    The factorial of a number, n, is its product with all the integers between 0 and n.

svg viewer

The factorial for 0 and 1 is always 1.
Sample Input#

n = 5

Sample Output#

120
"""


def factorial(n):
    # Replace with your own code
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
