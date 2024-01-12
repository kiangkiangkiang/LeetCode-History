from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        counter = 0
        current_accumulate = 0
        while counter < len(nums):
            if current_accumulate > 2:
                nums.pop(counter)
            else:
                if nums[counter] == prev:
                    current_accumulate += 1
                else:
                    current_accumulate = 1
                counter += 1


nums = [1, 1, 2, 3, 4]
a = Solution()
print(a.removeDuplicates(nums))
