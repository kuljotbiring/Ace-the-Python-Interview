"""
Given a string containing only square brackets, [], you must check whether the brackets are balanced or not. The
brackets are said to be balanced if, for every opening bracket, there is a closing bracket.

You will write your code in the check_balance() function, which returns True if the brackets are balanced and False if
they are not.

For an empty string, the function will return True.

For the sake of simplicity, you can assume that the string will not contain any other characters.

Sample Input

"[[[[][]]]]"

Sample Output#

True
"""


def check_balance(brackets):
    left_bracket = 0
    right_bracket = 0

    for char in brackets:
        if char == "[":
            left_bracket += 1
        elif char == "]":
            right_bracket += 1

    return left_bracket == right_bracket


print(check_balance("[[[[][]]]]"))
