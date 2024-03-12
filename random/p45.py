from collections import deque
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        memory = deque()
        if len(nums) == 1:
            return 0

        for i, current_num in enumerate(reversed(nums[:-1])):
            dist_to_final = i + 1
            if current_num >= dist_to_final:
                memory.appendleft(1)
            else:
                if (add_step := list(memory)[:current_num]) and (add_step := list(filter(lambda x: x != -1, add_step))):
                    memory.appendleft(1 + min(add_step))
                else:
                    memory.appendleft(-1)

        return memory[0]


nums = [2, 3, 1, 1, 4]
nums = [2, 3, 0, 1, 4]
nums = [0]
nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
a = Solution()
print(a.jump(nums=nums))
