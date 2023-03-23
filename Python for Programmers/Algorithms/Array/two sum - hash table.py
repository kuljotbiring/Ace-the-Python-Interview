"""
Given an array of integers, return True or False if the array has two numbers that add up to a specific
target. You may assume that each input would have exactly one solution.
"""


def two_sum(arr, target_val):

    diff_map = {}

    for idx, num in enumerate(arr):
        diff = target_val - num
        if diff in diff_map:
            return True
        diff_map[num] = idx
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum(A, target))
