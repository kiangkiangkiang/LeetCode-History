# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0

from typing import List


class Solution:
    def get_all_combination(self, mylist):
        pass

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        total = 1
        tmp_list = []
        result = 0
        for num in nums:
            if total * num < k:
                tmp_list.append(num)
                total *= num
            else:
                
        pass


nums = [10, 5, 2, 6]
k = 100
a = Solution()
print(a.numSubarrayProductLessThanK(nums, k))
