from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_sum = 1
        prev = None
        counter = 0
        while counter < len(nums):
            if nums[counter] == prev:
                if prev_sum < 2:
                    prev_sum += 1
                else:
                    
            else:
                prev_sum = 1


nums = [1, 1, 2, 3, 4]
a = Solution()
print(a.removeDuplicates(nums))
