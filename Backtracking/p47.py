from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        current, stack, result = [], [], []
        self.total = len(nums)
        self.raw_nums = nums[:]
        while nums:
            current.append(nums.pop(0))
            stack.append(nums[:])
            if len(current) == self.total:
                if current not in result:
                    result.append(current)
        return result


nums = [1, 1, 2]
a = Solution()
print(a.permute(nums))
