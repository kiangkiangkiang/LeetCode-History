from typing import List


class Solution:
    def scale(self, current, stack):
        new_nums, this_road = None, []
        counter = 0
        while stack:
            other_road = stack.pop()
            counter += 1
            if not other_road:
                continue
            else:
                if len(other_road) == 1:
                    this_road = other_road
                    stack.append([])
                else:
                    this_road = [other_road.pop()]
                    stack.append(other_road)
                break
        if this_road:
            current = current[: (self.total - counter)] + this_road
            new_nums = [i for i in self.raw_nums if i not in current]
            return new_nums, current, stack
        else:
            return None, None, None

    def permute(self, nums: List[int]) -> List[List[int]]:
        stack, result, current = [], [], []
        self.total = len(nums)
        self.raw_nums = nums[:]
        while nums:
            current.append(nums.pop(0))
            stack.append(nums[:])
            if len(current) == self.total:
                result.append(current)
                if stack:
                    nums, current, stack = self.scale(current, stack)

        return result


nums = [1, 1, 2, 3]
a = Solution()
print(a.permute(nums))
