# O(n) solution for finding maximum subarray of size K

def maximum_sum(array, k):
    # get the length of the array
    arr_len = len(array)

    # n must be larger than K
    if arr_len < k:
        print("Invalid - subset exceeds array size")
        return -1

    # get the sum of the first window
    window_sum = sum(array[:k])

    # set max sum to the first sum we can get
    max_sum = window_sum

    # iterate through the list in sections.
    for i in range(arr_len - k):
        # update window_sum by dropping left-most number and adding next to the right
        window_sum = window_sum - array[i] + array[i + k]
        # update max sum if window_sum was bigger
        max_sum = max(window_sum, max_sum)

    return max_sum


# code to instantiate
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maximum_sum(arr, k))
