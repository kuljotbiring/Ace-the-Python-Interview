"""
Implement a function that removes all the even elements from a given list. Name it remove_even(lst).
Input:
A list with random integers.

Output:
A list with only odd integers
"""
my_list = [1, 2, 4, 5, 10, 6, 3]


# use list comprehension to get a new list without evens
def remove_even(lst):
    # Write your code here!
    odd_list = [value for value in lst if value % 2 != 0]

    return odd_list


print(remove_even(my_list))
