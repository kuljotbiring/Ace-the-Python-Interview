"""
Given an array of integers, return True or False if the array has two numbers that add up to a specific
target. You may assume that each input would have exactly one solution.
"""


# array has to be sorted in ascending order for this to work
def two_sum(arr, target_val):

    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum(A, target))
