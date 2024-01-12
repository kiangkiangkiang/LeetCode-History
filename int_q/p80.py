from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        counter = 0
        current_accumulate = 0
        while counter < len(nums):
            if nums[counter] == prev:
                current_accumulate += 1
            else:
                current_accumulate = 1

            prev = nums[counter]

            if current_accumulate > 2:
                nums.pop(counter)
            else:
                counter += 1

        return len(nums)


nums = [1, 1, 1]
a = Solution()
print(a.removeDuplicates(nums))
print(nums)
