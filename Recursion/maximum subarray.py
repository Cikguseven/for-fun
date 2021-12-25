# HackerRank
# Given an array of integers, find the maximum possible sum among all nonempty
# subsequences (any subset) and all nonempty subarrays (contiguous subsequence)

def max_sum(int_array):
    current_max_subarray = max_subarr = max_subseq = -10001
    for n in int_array:
        # Check if existing sum should include current integer or restart the
        # sum from this integer to get maximum sum
        current_max_subarray = max(n, current_max_subarray + n)
        max_subarr = max(current_max_subarray, max_subarr)
        max_subseq = max(n, max_subseq, max_subseq + n)
    return [max_subarr, max_subseq]


n = [-2, -3, -1, -4, -6]

print(max_sum(n))
