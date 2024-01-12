from collections import Counter
from typing import List

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = len(nums) / 2
        for k, v in Counter(nums).items():
            if v > times:
                return k


nums = [3, 2, 3]
a = Solution()
print(a.majorityElement(nums))
