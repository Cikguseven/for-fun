# LeetCode 152
# Given an array of integers, find the maximum possible product among all
# nonempty subarrays (contiguous subsequence).

def max_product(int_array):
    max_subarray = min_subarray = max_product = int_array[0]
    int_array.pop(0)
    for n in int_array:
        x = max(n, max_subarray * n, min_subarray * n)
        y = min(n, max_subarray * n, min_subarray * n)
        max_subarray = x
        min_subarray = y
        max_product = max(max_subarray, max_product)
    return max_product


n = [-2, -3, -9, 0, -4, -6]

print(max_product(n))
