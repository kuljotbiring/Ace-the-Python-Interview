"""
You must implement the count_low_high() function. Its parameter is a list of numbers.

If a number is greater than 50 or divisible by 3, it will count as a high. If these conditions are not met, the number
is considered a low.

At the end of the function, you must return a list that contains the number of lows and highs, in that order.

In case the list is empty, you may return None.

Sample Input
num_list = [20, 9, 51, 81, 50, 42, 77]

Sample Output
[2, 5] # 2 lows and 5 highs
"""


def count_low_high(num_list):
    high = 0
    low = 0
    results = []
    if num_list is None:
        return None
    else:
        for number in num_list:
            if number > 50 or number % 3 == 0:
                high += 1
            else:
                low += 1

        results.append(low)
        results.append(high)

    return results


num_list = [20, 9, 51, 81, 50, 42, 77]
print(count_low_high(num_list))

num_list = [-10, 90, 15, 43]
print(count_low_high(num_list))
