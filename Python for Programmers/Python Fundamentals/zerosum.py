"""
You must implement the check_sum() function which takes in a list and returns True if the sum of two numbers in the list
is zero. If no such pair exists, return False.

Sample Input

[10, -14, 26, 5, -3, 13, -5]

Sample Output

True
"""


def check_sum(num_list):
    for i in range(0, len(num_list)):
        for j in range(1, len(num_list)):
            if num_list[i] + num_list [j] == 0:
                return True
    return False


# Should return True
print(check_sum([10, -14, 26, 5, -3, 13, -5]))

# Should return False
print(check_sum([10, -14, 26, 5, -3]))
