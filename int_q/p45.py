from typing import List

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:

# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.


class Solution:
    def jump(self, nums: List[int]) -> int:
        zero_locate = []
        prev_value = None
        counter = 0
        for i, v in enumerate(nums):
            if prev_value != 0:
                if v == 0:
                    zero_locate.append([i, i + 1])
                    counter += 1
            else:
                if v == 0:
                    zero_locate[counter - 1][1] += 1
            prev_value = v

        if len(nums) == 1:
            return 1

        for each_zero_locate in zero_locate:
            if not self.can_reach_end(nums[: each_zero_locate[0]], end=each_zero_locate[1]):
                return False
        return True


nums = [2, 3, 1, 1, 4]
a = Solution()
print(a.jump(nums))
