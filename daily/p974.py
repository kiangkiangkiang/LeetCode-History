# 974. Subarray Sums Divisible by K
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k,
# return the number of non-empty subarrays
# that have a sum divisible by k.

# A subarray is a contiguous part of an array.


# Example 1:

# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
# Example 2:

# Input: nums = [5], k = 9
# Output: 0

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        candidate = []
        pointer = 0
        while pointer < len(nums):
            if pointer >= 1:
                tmp = []
                for i in range(len(candidate)):
                    tmp.append(candidate[i] + [nums[pointer]])
                candidate.extend(tmp)

            candidate.append([nums[pointer]])
            pointer += 1
        print(123)
        return candidate


nums = [4, 5, 0, -2, -3, 1]
k = 5
a = Solution()
print(a.subarraysDivByK(nums, k))
