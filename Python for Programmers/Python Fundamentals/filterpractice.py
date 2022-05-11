"""
filter() function. It requires a function and a list.

filter() filters elements from a list if the elements satisfy the condition that is specified in the argument function.
"""

numList = [30, 2, -15, 17, 9, 100]

# returns a list which is of numbers greater than 10 - had to use the list function
greater_than_10 = list(filter(lambda n: n > 10, numList))
print(greater_than_10)