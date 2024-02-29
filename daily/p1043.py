from typing import List

# Given an integer array arr, partition the array into (contiguous) subarrays of length at most k.
# After partitioning, each subarray has their values changed to become the maximum value of that subarray.

# Return the largest sum of the given array after partitioning.
# Test cases are generated so that the answer fits in a 32-bit integer.

# Example 1:

# Input: arr = [1,15,7,9,2,5,10], k = 3
# Output: 84
# Explanation: arr becomes [15,15,15,9,10,10,10]
# Example 2:
54 + 28 + 1
# Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
# Output: 83
# Example 3:

# Input: arr = [1], k = 1
# Output: 1


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            maximum = 0
            max_sum = 0
            for j in range(1, k + 1):
                if i - j >= 0:
                    maximum = max(maximum, arr[i - j])
                    max_sum = max(max_sum, dp[i - j] + maximum * j)

            dp[i] = max_sum

        return dp[n]
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        max_sum = 0
        for i, ele in enumerate(arr):
            current_arr = arr[:i]
            if len(current_arr) <= k:
                max_sum = max(current_arr) * len(current_arr)
            else:
                

arr = [1, 15, 7, 9, 2, 5, 10]
k = 3

arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
k = 4
a = Solution()
print(a.maxSumAfterPartitioning(arr, k))
