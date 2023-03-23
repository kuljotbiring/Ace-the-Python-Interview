"""
Given an array of integers, return True or False if the array has two numbers that add up to a specific
target. You may assume that each input would have exactly one solution.
"""


def two_sum(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum(A, target))
target = 20
print(two_sum(A, target))
