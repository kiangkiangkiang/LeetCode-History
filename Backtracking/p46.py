from typing import List


class Solution:
    def p(self, nums: List[int]) -> List[List[int]]:
        result, remain_permute = [], []
        total_len = len(nums)
        current_result = []
        while True:
            current = nums.pop(0)
            if nums:
                remain_permute.append(nums)
            current_result.append(current)
            if len(current_result) == total_len:
                result.append(current_result)
                if remain_permute


nums = [0, 1]
a = Solution()
print(a.permute(nums))
