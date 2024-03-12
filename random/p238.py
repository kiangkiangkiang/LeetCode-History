from collections import deque
from typing import List

# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post_product = deque()
        prefix_product = []
        n = len(nums)
        tmp = 1
        for i in nums:
            tmp *= i
            prefix_product.append(tmp)

        tmp = 1
        for i in nums[::-1]:
            tmp *= i
            post_product.appendleft(tmp)

        result = []
        for i in range(n):
            if i == 0:
                result.append(post_product[i + 1])
            elif i == n - 1:
                result.append(prefix_product[i - 1])
            else:
                result.append(prefix_product[i - 1] * post_product[i + 1])
        return result


nums = [1, 2, 3, 4]
a = Solution()
print(a.productExceptSelf(nums))
