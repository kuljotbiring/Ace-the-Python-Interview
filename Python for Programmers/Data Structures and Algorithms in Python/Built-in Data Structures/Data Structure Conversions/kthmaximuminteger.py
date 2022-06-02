"""
Given a list of integers and a number k, find the kth largest integer in the list. The integer will be stored in the
kth_max variable.

For example, with a list of 7 integers, if k = 2, then kth_max will be equal to the second-largest integer in the list.
If k = 6, kth_max will equal the 6th largest integer.
"""

k = 2

test_list = [40, 35, 82, 14, 22, 66, 53]

test_list.sort(reverse=True)

kth_max = test_list[k - 1]

print(kth_max)
