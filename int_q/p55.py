from typing import List

# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


# out of memory
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_jumps = [nums[0]]
        n = len(nums) - 1

        if n == 0:
            return True

        current_positions = [0]
        while current_positions:
            stack = []
            next_pos = []
            for jumps, p in zip(current_jumps, current_positions):
                for i in range(jumps):
                    i = i + 1
                    if p + i < n:
                        stack.append(nums[p + i])
                        next_pos.append(p + i)
                    elif p + i == n:
                        return True
            current_jumps = stack
            current_positions = next_pos
        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) - 1 == 0:
            return True

        current_choice = nums[0]
        current_pos = 0
        stack, choice_memory = [], [nums[0]]
        while current_choice is not None:
            if current_pos == len(nums) - 1:
                return True
            elif current_pos > len(nums) - 1:
                # pop stack
                if stack:
                    other_tmp = stack.pop()
                    current_choice = nums[other_tmp.pop()]
                    current_pos -= choice_memory.pop()
                    current_pos += current_choice
                else:
                    return False
            else:
                # go ahead
                tmp = []
                for i in range(current_choice):
                    if i + 1 >= len(nums):
                        current_choice = len(nums) - current_pos - 1
                    else:
                        tmp.append(i + 1)
                breakpoint()
                current_pos += current_choice
                choice_memory.append(current_choice)
                current_choice = nums[tmp.pop()] if tmp else None
                if tmp:
                    stack.append(tmp)

        return False


class Solution:
    def can_reach_end(self, non_zero_nums, end):
        n = len(non_zero_nums)
        for i in range(n):
            if non_zero_nums[i] > end - 1 - i or non_zero_nums[i] == len(self.nums) - i - 1:
                return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
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

        if len(nums) == 1 or zero_locate == []:
            return True

        for each_zero_locate in zero_locate:
            if not self.can_reach_end(nums[: each_zero_locate[0]], end=each_zero_locate[1]):
                return False
        return True


# nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
# nums = [0]
nums = [1, 0, 1]
# nums = [2, 0]
# nums = [1, 1, 100, 0]
# nums = [1, 2, 3]
nums = [2, 0, 3, 0, 0, 0, 4]
# nums = [1, 2, 3, 0, 5, 4, 1, 3, 3]
# nums = [1, 1, 1, 0]
# nums = [2, 0, 0]
a = Solution()
print(a.canJump(nums))
